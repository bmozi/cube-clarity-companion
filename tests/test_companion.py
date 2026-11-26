"""Public lessons must work without manuscript files or production dependencies."""
from pathlib import Path
import json
import math
import re
import subprocess
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from cube_clarity.cube import sol,key,apply,inv
from cube_clarity.blindfold import load_routes,plan,execute,IDENTITY
from cube_clarity.pocket import CORNERS,solve
from cube_clarity.short_solutions import SUPERFLIP_SETUP,SOLUTION_GROUPS

class CompanionTests(unittest.TestCase):
    def command(self,*args):
        return subprocess.run([sys.executable,*args],cwd=ROOT,text=True,capture_output=True,check=True).stdout

    def test_lesson_links_assets_and_book_independence(self):
        for path in [ROOT/'README.md',ROOT/'CHANGELOG.md',*sorted((ROOT/'docs').glob('*.md'))]:
            content=path.read_text()
            self.assertNotRegex(content,r'\[FIGURE |(?:see|Use) Chapter \d+')
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',content):
                if re.match(r'https?://',target):continue
                file,_,anchor=target.partition('#');linked=(path.parent/file).resolve()
                self.assertTrue(linked.is_relative_to(ROOT.resolve()),(path,target))
                self.assertTrue(linked.is_file(),(path,target))
                if anchor:
                    titles=re.findall(r'(?m)^#+ (.+)$',linked.read_text())
                    anchors=[re.sub(r'[^\w\- ]','',t.lower()).replace(' ','-') for t in titles]
                    self.assertIn(anchor,anchors,(path,target))
            refs=set(re.findall(r'(?m)^\[(S?\d+)\]:',content))
            mentions=set(re.findall(r'(?<!\w)\[(S?\d+)\](?![:(])',content))
            self.assertLessEqual(mentions,refs,path)
        self.assertFalse((ROOT/'manuscript').exists())
        self.assertFalse((ROOT/'production').exists())
        self.assertFalse(any(ROOT.rglob('*.docx')))

    def test_pocket_published_trace_replays_and_matches_stage_checks(self):
        text=(ROOT/'docs/2x2-course.md').read_text();state=apply(CORNERS,'R U F2');goal=dict(CORNERS)
        rows=re.findall(r'(?m)^\| (\d+) \| ([^|]+) \| `([^`]+)` \|$',text)
        _,expected,trace=solve(state);self.assertEqual(len(rows),len(trace))
        for i,((number,stage,moves),step) in enumerate(zip(rows,trace),1):
            self.assertEqual(int(number),i);self.assertEqual(stage.strip(),step['stage']);self.assertEqual(moves,step['moves'])
            state=apply(state,moves)
            if moves=='y':goal=apply(goal,moves)
            self.assertEqual(state,step['state'])
        self.assertEqual(state,goal);self.assertEqual(state,expected)
        self.assertIn('all 24 corner stickers solved',self.command('examples/pocket_practice.py','--scramble','R U F2'))

    def test_all_published_blindfold_rows_and_worked_answers(self):
        text=(ROOT/'docs/blindfold-course.md').read_text();routes=load_routes()
        self.assertEqual(len(re.findall(r'(?m)^\| [A-X] \| [UDFBRL]{2,3} \| .+ \| (?:T|Corner engine) \|',text)),43)
        for family,plural in [('edge','edges'),('corner','corners')]:
            for address,letter in routes['letter_map'][family].items():self.assertIn(f'| {letter} | {address} |',text)
            for target,row in routes[family].items():
                self.assertIn(f'| {row["letter"]} | {target} | {row["setup"] or "None"} |',text)
            for ex in routes['worked_examples']:
                state=apply(IDENTITY,ex['scramble']);record=plan(state);self.assertEqual(execute(state,record),IDENTITY)
                self.assertEqual(record[plural]['targets'],ex['plan'][plural]['targets'])
                letters=' '.join(routes['letter_map'][family][x] for x in record[plural]['targets'])
                self.assertIn(f'| {family.title()} | {letters} |',text)
        output=self.command('examples/blindfold_practice.py','--scramble','F')
        self.assertIn('Edges targets: C F U P C',output)
        self.assertIn('edges; parity bridge; corners.',output)
        self.assertIn('all 54 stickers restored',output)

    def test_shorter_solution_lesson_checks_every_sticker_and_count(self):
        text=(ROOT/'docs/mathematics-and-shorter-solutions.md').read_text()
        self.assertEqual(math.factorial(8)*3**7*math.factorial(12)*2**10,43252003274489856000)
        self.assertIn('43,252,003,274,489,856,000',text)
        self.assertEqual(apply(apply(sol,'R U U'),"U2 R'"),sol)
        state=apply(sol,SUPERFLIP_SETUP)
        self.assertTrue(all(state[k]==v for k,v in sol.items() if sum(x*x for x in k[0])==3))
        self.assertTrue(all(state[k]!=v for k,v in sol.items() if sum(x*x for x in k[0])==2))
        for group in SOLUTION_GROUPS:
            state=apply(state,group);self.assertIn(group.replace("'",'′'),text)
        self.assertEqual(state,sol);self.assertEqual(len(' '.join(SOLUTION_GROUPS).split()),20)

    def test_case_tool_keeps_recognition_separate_from_practice_setups(self):
        lines=self.command('examples/case_practice.py','--list').splitlines();self.assertEqual(len(lines),119)
        hidden=self.command('examples/case_practice.py','--case','F2L-026','--hide-answer')
        self.assertNotIn('DO:',hidden);self.assertNotIn('PRACTICE ONLY:',hidden)
        shown=self.command('examples/case_practice.py','--case','F2L-026','--show-setup')
        self.assertIn("DO: R U' R'",shown);self.assertIn("apply: R U R'",shown)
        bad=subprocess.run([sys.executable,'examples/case_practice.py','--case','F2L-999'],cwd=ROOT,capture_output=True)
        self.assertEqual(bad.returncode,2)
        for example in json.loads((ROOT/'data/learning_transfer_cases.json').read_text()):
            rows=json.loads((ROOT/'data/f2l_working_cases.json').read_text());row=next(x for x in rows if x['id']==example['atlas_id'])
            self.assertEqual(apply(apply(sol,row['setup']),' '.join(example['groups'])),sol)

if __name__=='__main__':unittest.main()
