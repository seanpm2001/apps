# repo.roscidus.com

http://repo.roscidus.com/ provides [Zero Install](http://0install.net/) feeds for programs and libraries where the upstream authors do not provide feeds of their own. It also serves as a semi-official repository for basic infrastructure components such as libraries and runtime environments.

The feeds are updated using the following tools:

[0watch](https://github.com/0install/0watch) scrapes upstream websites to discover new versions of applications. It runs a watch file (e.g., `ffmpeg.watch.py`) and then automatically calls 0template as needed.

[0template](https://github.com/0install/0template) is used to add new releases of applications. It takes a template (e.g., `ffmpeg.xml.template`) and values for placeholders (e.g., a version number) as input and generates a new feed (e.g., `ffmpeg-2.0.0.xml`) as output.

[0repo](https://github.com/0install/0repo) merges feeds generated by 0template (e.g., `ffmpeg-2.0.0.xml`) into the appropriate main (e.g., `ffmpeg.xml`).

We run this process periodically in a [CI environment](https://ci.appveyor.com/project/0install/repo-roscidus-com). You can also try it out on your own machine:
- `git clone https://github.com/0install/repo.roscidus.com.git feeds`  
  Note: The target directory **must** be called `feeds`.
- `./watch.sh` for Linux or `.\watch.ps1` for Windows  
  Note: These two scripts/platforms update two different subsets of the feeds. To update everything you need to run both.
