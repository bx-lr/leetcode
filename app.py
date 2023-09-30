import os
import sys
import cmd2
import glob
import shutil
import traceback
import collections
import numpy as np
from rich.console import Console
from rich.table import Table
from libs.bandit import MultiArmedBandit


class LeetCodeRunner(cmd2.Cmd):
    '''Simple cmd2 application to test your leetcode ability'''
    def __init__(self, files):
        super().__init__(startup_script='.cmd2rc', silence_startup_script=True)
        # List of all files with full path
        self.files = files
        self.orig_prompt = '(Cmd) '
        # List of all categories
        self.categories = [fn.split(os.sep)[-2] for fn in self.files]
        # List of all questions, .py files
        self.specific_questions = [fn.split(os.sep)[-1] for fn in self.files]
        # List of selected questions, maybe not needed
        self.test_questions = []
        self.current_question_num = -1
        self.current_question = None
        # Lists to store rewards and optimal question selections over time
        self.bandit = None

        # import each question
        result = collections.defaultdict(list)
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
                result[category].append({'difficulty': difficulty,
                                         'category': category,
                                         'selected': False,
                                         'name': problem_name,
                                         'module': mod})
            except AttributeError:
                print(f'\t[ERROR] Unable to import problem: "{fn}"')
                print(sys.exc_info())
                continue

        # sort the results
        for k, v in result.items():
            sorted_values = sorted(v, key=lambda x: x['difficulty'])
            result[k] = sorted_values

        # Ordered list of all questions
        self.ordered_questions = result

        # User choices, settable using set command
        # used in:
        # do_select
        # do_clear
        # get_test_questions
        self.selection = []

        self.add_settable(cmd2.Settable('selection',
                                        list,
                                        'Question category or specific question for run command',
                                        self))

        # Make question difficulty minimum settable at runtime
        # used in:
        # do_select
        # do_clear
        # get_test_questions
        self.question_difficulty_min = 1.0
        self.add_settable(cmd2.Settable('question_difficulty_min',
                                        float,
                                        'Minimum difficulty for run command',
                                        self))

        # Make question difficulty minimum settable at runtime
        # used in:
        # do_select
        # do_clear
        # get_test_questions
        self.question_difficulty_max = 4.0
        self.add_settable(cmd2.Settable('question_difficulty_max',
                                        float,
                                        'Maximum difficulty for run command',
                                        self))

    def category_provider(self):
        '''returns list of available question categories'''
        return self.categories

    def question_provider(self):
        '''returns list of available questions'''
        return self.specific_questions

    def get_test_questions(self, filter):
        '''updates selected question status'''
        if filter:
            if len(self.selection) > 0:
                # category was set
                for item in self.selection:
                    for question in self.ordered_questions[item]:
                        difficulty = question.get('difficulty', 0)
                        # filter by difficulty
                        if difficulty > self.question_difficulty_min and \
                           difficulty < self.question_difficulty_max:
                            question['selected'] = True
                            #only add unique items
                            if question not in self.test_questions:
                                self.test_questions.append(question)
            else:
                # only min/max was set
                for value in self.ordered_questions.values():
                    for question in value:
                        difficulty = question.get('difficulty', 0)
                        # filter by difficulty
                        if difficulty > self.question_difficulty_min and \
                           difficulty < self.question_difficulty_max:
                            question['selected'] = True
                            # only add uniuqe items
                            if question not in self.test_questions:
                                self.test_questions.append(question)
        else:
            # question was set
            for value in self.ordered_questions.values():
                for question in value:
                    # update the status of the question 
                    if question.get('name', '')+'.py' in self.selection:
                        question['selected'] = True
                        # only add unique items
                        if question not in self.test_questions:
                            self.test_questions.append(question)
        if len(self.test_questions) > 0:
            self.bandit = MultiArmedBandit(len(self.test_questions))
        return

    # argparser for do_select
    select_parser = cmd2.Cmd2ArgumentParser()
    select_parser.add_argument('-c',
                               '--category',
                               nargs='+',
                               choices_provider=category_provider,
                               help='Question cateogry selection')

    select_parser.add_argument('-q',
                               '--question',
                               nargs='+',
                               choices_provider=question_provider,
                               help='Specific question selection')

    select_parser.add_argument('-n',
                               '--min',
                               default=1.0,
                               type=float,
                               help='Minimum question difficulty')

    select_parser.add_argument('-m',
                               '--max',
                               default=4.0,
                               type=float,
                               help='Maximum question difficulty')

    @cmd2.with_argparser(select_parser)
    def do_select(self, args):
        '''Select question categories or specific questions to test'''
        if args.category:
            self.question_difficulty_min = args.min
            self.question_difficulty_max = args.max
            do_filter = True
            self.selection = self.selection + args.category
        elif args.question:
            self.selection = self.selection + args.question
            do_filter = False
        elif args.min or args.max:
            do_filter = True
            self.question_difficulty_min = args.min
            self.question_difficulty_max = args.max
        else:
            print('Please select a question or a category')
            return
        # get test questions based on filter criteria
        self.get_test_questions(do_filter)
        return

    def get_bandit_question(self):
        '''Use the bandit to select a question'''
        # Get the question with the lowest score
        #q_num = self.bandit.choose_question()
        q_num = self.bandit.choose_question_2()
        # get actual question and update current
        question = self.test_questions[q_num]
        self.current_question = question
        self.current_question_num = q_num
        return question

    def update_bandit(self, success):
        '''updates the bandit based on how we did'''
        # update the question score based on how we did
        self.bandit.update(self.current_question_num, success)
        #self.bandit.update_2(self.current_question_num, success)
        self.bandit.question_attempts[self.current_question_num] += 1
        self.bandit.total_successes.append(success)
        return

    def do_run(self, args):
        '''Use the bandit to grab a question, generate scratch_pad.py file'''
        if not self.bandit:
            print('Use the select command to select a question first')
            return
        question = self.get_bandit_question()
        print(question)
        self.prompt = f'({question["name"]}) '
        # create solution file
        print('\n\n**** Emitting problem file: "scratch_pad.py" ****')
        print('\nProblem Description: \n')
        # print question instructions
        print(question['module'].get_instructions())
        # copy the test file (where the answer goes)
        shutil.copy2(question['module'].__file__, 'scratch_pad.py')
        return

    def do_check(self, args):
        '''Check scratch_pad.py and update the bandit'''
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
            module = self.current_question.get('module', None)
            if module:
                print(f'Source file: "{module.__file__}"')
        # update the score
        if was_wrong:
            # failed to answer correctly
            module = self.current_question.get('module', None)
            print(module.get_solution())
            self.update_bandit(0)
        else:
            # answered correctly
            self.update_bandit(1)
        # better update function
        # todo: move into update_bandit
        self.bandit.update_2(self.current_question_num, was_wrong)
        self.prompt = self.orig_prompt
        return

    # argparser for do_list
    list_parser = cmd2.Cmd2ArgumentParser()
    list_parser.add_argument('-a',
                             '--all',
                             action='store_true',
                             help='Print all questions')

    @cmd2.with_argparser(list_parser)
    def do_list(self, args):
        '''pretty print selected questions'''
        # TODO: add check for --all flag
        # otherwise we should only print the ones with
        # selected==True
        for cat in self.ordered_questions.keys():
            cols = list(self.ordered_questions[cat][0].keys())
            table = Table(title=cat, min_width=100)

            for i in range(len(cols)-1):
                table.add_column(cols[i])

            for line in self.ordered_questions[cat]:
                vals = [str(v) for v in line.values()]
                if vals[2] == 'True':
                    table.add_row(f'[green]{vals[0]}[/]',
                                  f'[green]{vals[1]}[/]',
                                  f'[green]{vals[2]}[/]',
                                  f'[green]{vals[3]}[/]')
                else:
                    table.add_row(vals[0], vals[1], vals[2], vals[3])
            console = Console()
            console.print(table)
        return

    def do_clear(self, args):
        '''Clear questions/categories, reset min/max levels, clear bandit'''
        # zero all values
        self.selection = []
        self.question_difficulty_min = 1.0
        self.question_difficulty_max = 4.0
        self.bandit = None
        self.optimal_selections = []
        self.test_questions = []
        self.current_question_num = -1
        self.current_question = None
        return

    def do_status(self, args):
        '''Prints out the current run status'''
        if len(self.test_questions) < 1:
            print('No current run, use "select" and "run" to test yourself')
            return
        # get the column names
        cols = list(self.test_questions[0].keys())[:-1]
        cols.append('attempts')
        cols.append('success rate')
        table = Table(title='Test Results', min_width=100)
        # update the table columns
        for c in cols:
            table.add_column(c)
        # add data to the table
        for question, attempts, success, in zip(self.test_questions,
                                                self.bandit.question_attempts,
                                                self.bandit.estimated_success_rates):
            # pull out the values to print
            difficulty = question.get('difficulty', -1)
            category = question.get('category', -1)
            selected = question.get('selected', -1)
            name = question.get('name', -1)

            if success < 0.9 and attempts > 0.0:
                # tested poorly
                table.add_row(f'[red]{difficulty}[/]',
                              f'[red]{category}[/]',
                              f'[red]{selected}[/]',
                              f'[red]{name}[/]',
                              f'[red]{attempts}[/]',
                              f'[red]{success}[/]')
            elif success == 0.0:
                # untested
                table.add_row(f'{difficulty}',
                              f'{category}',
                              f'{selected}',
                              f'{name}',
                              f'{attempts}',
                              f'{success}')
            else:
                # good test
                table.add_row(f'[green]{difficulty}[/]',
                              f'[green]{category}[/]',
                              f'[green]{selected}[/]',
                              f'[green]{name}[/]',
                              f'[green]{attempts}[/]',
                              f'[green]{success}[/]')
        # print the results
        console = Console()
        console.print(table)
        return


if __name__ == '__main__':
    # get all questions
    files = [fn for fn in
             glob.glob('questions/**', recursive=True)
             if fn.endswith('.py')]

    # adjust the path so we can find the questions
    _ = [sys.path.append(f) for f in glob.glob('questions/**')]

    # start it up
    lcr = LeetCodeRunner(files)
    sys.exit(lcr.cmdloop())
