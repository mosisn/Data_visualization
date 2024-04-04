import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars'

headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url=url, headers=headers)
print(f'status code: {r.status_code}')
response_dict = r.json()
print(f'Total Reposetories: {response_dict['total_count']}')
print(f'Compelete Results: {response_dict['incomplete_results']}')
repo_dicts = response_dict['items']
print(f'reposetories returned: {len(repo_dicts)}')
# repo_dict = repo_dicts[0]
# print(f'Keys:{len(repo_dict)}')
for repo_dict in repo_dicts:
    print('\n Selected information for each reposetory:')
    print(f'name: {repo_dict['name']}')
    print(f'owner: {repo_dict['owner']['login']}')
    print(f'stars: {repo_dict['stargazers_count']}')
    print(f'reposetory: {repo_dict['html_url']}')
    print(f'created: {repo_dict['created_at']}')
    print(f'updated: {repo_dict['updated_at']}')
    print(f'description: {repo_dict['description']}')

