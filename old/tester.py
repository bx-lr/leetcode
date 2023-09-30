import os
import sys
import signal
import collections
import argparse
import rich
import math
import shutil
from typing import *
import glob
import argparse
import traceback

'''
multi-armed bandit Q/A on leetcode questions
'''


def get_all_questions() -> dict:
    '''
    returns a result dict with the following structure
    keys = problem type
    values = [problem difficulty, script file, imported module]

    each problem should contain:
    - get_difficulty()
    - get_instructions()
    - get_template()
    - get_check()
    '''
    result = collections.defaultdict(list)

    files = [fn for fn in glob.glob('questions/**', recursive=True) if fn.endswith('.py')]
    _ = [sys.path.append(f) for f in glob.glob('questions/**')]
    for fn in files:
        # get the folder and file name
        fpath = fn.split(os.sep)
        # import the script
        try:
            mod = (__import__(fpath[-1].rstrip('.py')))
            # get the difficulty, problem name, and category
            difficulty = mod.get_difficulty()
            problem_name = fpath[-1].rstrip('.py')
            category = fpath[1]
            # add to the results
            result[category].append({'difficulty': difficulty, 'category': category, 'name': problem_name, 'module': mod})
        except AttributeError as e:
            print(f'\t[ERROR] Unable to import problem: "{fn}"')
            continue
    # sort the results
    for k, v in result.items():
        sorted_values = sorted(v, key=lambda x: x['difficulty'])
        result[k] = sorted_values
    return result


# ask question
def run_bandit(problems: list):
    names = [p.get('name') for p in problems]
    modules = [p.get('module') for p in problems]
    data = [[0] for _ in names]
    done = False

    # simple signal handler to print out our success / failure rates
    # once we are done testing
    def signal_handler(sig, frame):
        print('Exiting, heres your summary:')
        for d, n in zip(data, names):
            print(f'\tResult for problem: {n}')

            if len(d) - 1 > 0:
                print(f'\tNumber of tests: {len(d)-1}, Pass rate: {(1 - sum(d) / (len(d)-1)) * 100}%')
            else:
                print('\tNot tested')
            print(d)
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    # main problem solving loop
    while not done:
        tmp_row_values = []
        for idx in range(len(names)):
            if len(data[idx]) == 1:  # never seen this problem before
                tmp_row_values.append(1000)
            else:
                # calculate our score
                score = ((sum(data[idx]) / len(data[idx])) + (math.sqrt(2 * math.log(sum([len(x) for x in data])+1) / len(data[idx]))))
                tmp_row_values.append(score)
        # find optimal question (one with most wrong answers)
        max_idx = tmp_row_values.index(max(tmp_row_values))
        # create solution file
        print('\n\n**** Emitting problem file: "scratch_pad.py" ****')
        print('\nProblem Description: \n')
        print(modules[max_idx].get_instructions())
        shutil.copy2(modules[max_idx].__file__, 'scratch_pad.py')
        # test the solution
        _ = input('Press enter to test your solution: ')
        was_wrong = 1
        # remove and re-import the module
        try:
            if 'scratch_pad' in sys.modules:
                del sys.modules['scratch_pad']
            from scratch_pad import Solution
            sol = Solution()
            was_wrong = sol.check()
            del sol
        except Exception:
            # something went wrong, maybe a typo... idk
            print(sys.exc_info())
            traceback.print_exc()
            print(f'Source file: "{modules[max_idx].__file__}"')
        # update the score
        if was_wrong:
            # todo: print diff of source file get_solution() results with solution code from scratch_pad.py
            # todo: add pretty colors
            print(modules[max_idx].get_solution())
            _ = input('Press enter to continue...')
        data[max_idx].append(was_wrong)
    return


def main():
    print('Importing questions...')
    questions = get_all_questions()
    print('Loaded the following:')
    for k, v in questions.items():
        print(f'\tCategory: {k}')
        for item in v:
            print(f'\t\tProblem: {item["name"]}')
            print(f'\t\tDifficulty: {item["difficulty"]}')
    categories = []
    problems = []
    # get the input category
    while len(categories) < 1:
        inp = input('What group would you like to evaluate?\nInput the name or press enter for all: ')
        if inp:
            # find our category
            categories = questions.get(inp, [])
            categories = set([cat.get('category', '') for cat in categories])
        else:
            categories = questions.keys()
        # couldn't find the category
        if len(categories) < 1:
            print(f'Unknown group "{inp}", try again')
    # get the input problem level
    while len(problems) < 1:
        # todo: use argparse to select range of problems
        # e.g. -ge 1 -le 2.5
        dif = input('What difficulty level would you like to evaluate?\nInput number (1-3, lowest=easiest, supports --ge 1.0 --le 2.5 range) or press enter for all: ')
        # cast our stuff
        start, stop = 0.0, 0.0
        if len(dif) < 1:
            dif = -1
        else:
            dif = dif.split(' ')
            for i in range(len(dif)):
                if dif[i].find('le') > -1 or dif[i] == '<':
                    stop = float(dif[i+1])
                elif dif[i].find('ge') > -1 or dif[i] == '>':
                    start = float(dif[i+1])
                else:
                    continue

        # get the selected problems
        for cat in categories:
            for item in questions[cat]:
                # handle case when difficulty is a single number
                if type(dif) == type(0.0):
                    if dif < 0.0 or (dif == item.get('difficulty', 0.0)):
                        problems.append(item)
                # handle range
                elif stop > 0.0:
                    if (item.get('difficulty', 0.0) <= stop) and (item.get('difficulty', 0.0) >= start):
                        problems.append(item)
                else:
                    continue
    # start the bandit
    run_bandit(problems=problems)
    return


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    main()
# autodocstring
# bettercomments
# todostring? todotree
# rewrap