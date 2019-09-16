import jiraautomation.operations
import jiraautomation.console.command_line
import jacustomization.operations.count_issues

def main():
    jiraautomation.operations.register.register(jacustomization.operations.count_issues.count_issues)
    jiraautomation.console.command_line.main()
    
if __name__ == "__main__":
    main()