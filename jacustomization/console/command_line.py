import jiraautomation.operations
import arcjiraautomation.operations.issues_comparison
import jiraautomation.console.command_line

def main():
    jiraautomation.operations.register.register(jacustomization.operations.count_issues.count_issues)
    jiraautomation.console.command_line.main()
    
if __name__ == "__main__":
    main()