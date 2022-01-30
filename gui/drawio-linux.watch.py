#os=Linux
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import github

excluded_versions = ['v15.3.7']

releases = [{
    'version': release['tag_name'].strip('v'),
    'released': release['published_at'][0:10]
} for release in github.releases('jgraph/drawio-desktop') if not release['prerelease'] and not release['tag_name'] in excluded_versions and any(asset['name'].endswith('.deb') for asset in release['assets'])]
