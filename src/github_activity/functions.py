from . import api

#Eventos de interação com o código:

def _format_create_event(event: dict) -> str:
    """Formats a CreateEvent into a readable string"""
    repo_name = event["repo"]["name"]
    return f"- Repo {repo_name} created"

def _format_push_event(event: dict) -> str:
    """Formats a PushEvent into a readable string."""
    repo_name = event["repo"]["name"]
    return f"- Pushed commit to {repo_name}"

def _format_delete_event(event: dict) -> str:
    """Formats a DeleteEvent into a readable string"""
    repo_name = event["repo"]["name"]
    item_deleted = event["payload"]["ref"]
    return f"- {item_deleted.capitalize()} deleted at Repo {repo_name}"

def _format_fork_event(event: dict) -> str:
    """Formats a ForkEvent into a readable string"""
    repo_name = event["repo"]["name"]
    new_repo_name = event["payload"]["name"]
    return f"- Copy of Repo{repo_name} created. The new Repo name is {new_repo_name}"

#Eventos de Issues e Pull Requests

def _format_issues_event(event: dict) -> str:
    """Formats an IssuesEvent into a readable string."""
    action = event["payload"]["action"]
    repo_name = event["repo"]["name"]
    issue_number = event["payload"]["issue"]["number"]
    return f"- {action.capitalize()} issue #{issue_number} in {repo_name}"

def _format_issues_comment_event(event: dict) -> str:
    """Formats an IssueCommentEvent into a readable string."""
    action = event["payload"]["action"]
    repo_name = event["repo"]["name"]
    issue_number = event["payload"]["issue"]["number"]
    return f"- {action.capitalize()} comment on issue #{issue_number} in {repo_name}"

def _format_pull_request_event(event: dict) -> str:
    """Formats a PullRequestEvent into a readable string."""
    action = event["payload"]["action"]
    repo_name = event["repo"]["name"]
    pr_number = event["payload"]["number"]
    return f"- {action.capitalize()} pull request #{pr_number} in {repo_name}"

def _format_pull_request_review_event(event: dict) -> str:
    """Formats a PullRequestReviewEvent into a readable string."""
    action = event["payload"]["action"]
    repo_name = event["repo"]["name"]
    pr_number = event["payload"]["pull_request"]["number"]
    return f"- {action.capitalize()} a review on pull request #{pr_number} in {repo_name}"

def _format_pull_request_review_comment_event(event: dict) -> str:
    """Formats a PullRequestReviewCommentEvent into a readable string."""
    action = event["payload"]["action"]
    repo_name = event["repo"]["name"]
    pr_number = event["payload"]["pull_request"]["number"]
    return f"- {action.capitalize()} a review comment on pull request #{pr_number} in {repo_name}"

#Eventos Sociais e de comunidade

def _format_watch_event(event: dict) -> str:
    """Formats a WatchEvent into a readable string."""
    repo_name = event["repo"]["name"]
    return f"- Starred {repo_name}"

def _format_member_event(event: dict) -> str:
    """Formats a MemberEvent into a readable string."""
    action = event["payload"]["action"]
    repo_name = event["repo"]["name"]
    member_login = event["payload"]["login"]
    if action == "added":
        return f"- New member {member_login} was {action} to {repo_name}"
    elif action == "deleted":
        return f"- Member {member_login} was {action} from {repo_name}"
    else:
        return f"- Member {member_login} was {action} in {repo_name}"
    
def _format_sponsorship_event(event: dict) -> str:
    """Formats a SponsorshipEvent into a readable string."""
    repo_name = event["repo"]["name"]
    action = event["payload"]["action"]
    sponsor_name = event["payload"]["sponsorship"]["sponsor"]["login"]
    if action == "tier_changed":
        return f"- Sponsor {sponsor_name} {action.capitalize()} in {repo_name}"
    else:    
        return f"- Sponsor {sponsor_name} {action.capitalize()} a sponsorship in {repo_name}"
    
def _format_public_event(event: dict) -> str:
    """Formats a PublicEvent into a readable string."""
    return "- Repositório se tornou público"

# Eventos de conteúdo e outros

def _format_gollum_event(event: dict) -> str:
    """Formats a GollumEvent into a readable string."""
    repo_name = event["repo"]["name"]
    action = event["pages"]["action"]
    page_name = event["pages"]["page_name"]

    return f"- Page {page_name} of Repo{repo_name} was {action}"

def _format_release_event(event: dict) -> str:
    """Formats a ReleaseEvent into a readable string."""
    repo_name = event["repo"]["name"]
    action = event["pages"]["action"]
    return f"- A new release of the Repo {repo_name} was {action}"

def _format_commit_comment_event(event: dict) -> str:
    """Formats a CommitCommentEvent into a readable string."""
    repo_name = event["repo"]["name"]
    action = event["pages"]["action"]
    return f"- A commit was {action} at the Repo {repo_name}"



# Map event types to their formatting functions
EVENT_HANDLERS = {
    "CommitCommentEvent": _format_commit_comment_event,
    "CreateEvent": _format_create_event,
    "DeleteEvent": _format_delete_event,
    "ForkEvent": _format_fork_event,
    "GollumEvent": _format_gollum_event,
    "IssueCommentEvent": _format_issues_comment_event,
    "IssuesEvent": _format_issues_event,
    "MemberEvent": _format_member_event,
    "PublicEvent": _format_public_event,
    "PullRequestEvent": _format_pull_request_event,
    "PullRequestReviewEvent": _format_pull_request_review_event,
    "PullRequestReviewCommentEvent": _format_pull_request_review_comment_event,
    "PushEvent": _format_push_event,
    "ReleaseEvent": _format_release_event,
    "SponsorshipEvent": _format_sponsorship_event,
    "WatchEvent": _format_watch_event,
}


def getEvents(username: str):
    data = api.getUserData(username)

    for event in data:
        event_type = event["type"]
        handler = EVENT_HANDLERS.get(event_type)

        if handler:
            formatted_event = handler(event)
            print(formatted_event)