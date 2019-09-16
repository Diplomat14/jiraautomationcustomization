from jiraautomation.operations.operation import  basic_operation

class count_issues(basic_operation):

    __logger = None

    @staticmethod
    def name():
        return "CountIssues"

    @staticmethod
    def init_arguments(operation_group):
        # operations_group = parser.add_argument_group

        # Add your argparse parameters here
        # operations_group.add_argument('-param1', '--parameter1', required=True,
        #                                   help='Parameter1 Description')
        pass

    @staticmethod
    def parse_arguments(args):
        # You might want to prepare arguments somehow like:
        # args.operation = CoreOperation[args.operation]
        # TODO: Do i need to return? it is by reference actually
        pass

    def __init__(self, iLogger):
        super(issues_comparison,self).__init__(iLogger)

    def execute(self, container, args):
        l = self.logger

        try:
            jira = container.getJIRA()

            try:
                request_query = args.query
                # top_request_query = 'project = %s AND issuetype = "%s" ORDER BY updated DESC' % (projectId, topIssueType)
                issues = jira.search_issues_nolim(request_query)
                l.msg(str(len(issues)) + " issues found")

                return issues

            except Exception as e:
                l.error("Exception happened boards search " + str(e))

            # self.persistContainer()
        except Exception as e:
            l.error("Exception happened during connection establishment " + str(e))

