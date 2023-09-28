import os
import cmd2
import sys
import glob
import collections
from rich.console import Console
from rich.table import Table

class LeetCodeRunner(cmd2.Cmd):
    '''Simple cmd2 application to test your leetcode ability'''
    def __init__(self, files):
        super().__init__()
        self.files = files
        self.categories = [fn.split(os.sep)[-2] for fn in self.files]
        self.specific_questions = [fn.split(os.sep)[-1] for fn in self.files]
        self.do_filter = False

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

        # save off our ordered question list
        self.ordered_questions = result

        # Make question category settable at runtime
        self.selection = []

        self.add_settable(cmd2.Settable('selection',
                                        list,
                                        'Question category or specific question for run command',
                                        self))

        # Make question difficulty minimum settable at runtime
        self.question_difficulty_min = 1.0
        self.add_settable(cmd2.Settable('question_difficulty_min',
                                        float,
                                        'Minimum difficulty for run command',
                                        self))

        # Make question difficulty minimum settable at runtime
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

    def get_test_questions(self):
        '''returns list of selected questions'''
        return

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

    select_parser.add_argument('-i',
                               '--min',
                               default=1.0,
                               type=float,
                               help='Minimum question difficulty')

    select_parser.add_argument('-a',
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
            self.do_filter = True
            self.selection = args.category
        elif args.question:
            self.selection = args.question
            self.do_filter = False
        else:
            print('Please select a question or a category')
            return
        # call get_test_questions
        # print pretty table
        return

    # load_parser = cmd2.Cmd2ArgumentParser()
    # load_parser.add_argument('-c',
    #                            '--category',
    #                            nargs='+',
    #                            choices_provider=category_provider,
    #                            help='Load questions by category')

    # load_parser.add_argument('-q',
    #                            '--question',
    #                            nargs='+',
    #                            choices_provider=question_provider,
    #                            help='Load specific question')

#    @cmd2.with_argparser(load_parser)
#    def do_load(self, args):
#        '''Load questions by category or by specific question'''
#        if args.category:

    # do_run
    # select a questions and generate scratch_pad.py

    # do_check
    # check scratch_pad.py and update the bandit

    list_parser = cmd2.Cmd2ArgumentParser()
    list_parser.add_argument('-a',
                             '--all',
                             action='store_true',
                             help='Print all questions')

    @cmd2.with_argparser(list_parser)
    def do_list(self, args):
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

    # do_clear
    # clear selected category, min, max, or questions


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
