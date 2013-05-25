# Tab Count Logger

Tab Count Logger is a Firefox extension that periodically logs a count of open tabs/windows to an SQLite database. It was created because existing tab-counter extensions recorded only scalar statistics rather than a full history.

Currently it is hard-coded to collect a count once every 30 s.

# Build
To build, extract and activate the [Mozilla Add-on SDK](https://github.com/mozilla/addon-sdk), and run `cfx xpi` to generate the XPI.

# Usage
While the extension is installed and enabled, it will display "Tab Count Logger" in the status bar and log to an SQLite database  (table `tabCountLog` of `tabCountLog.sqlite` in your profile directory; both will be created if not already present). Clicking the text causes it to immediately record a count. To pause data collection, disable the extension.

There is no UI for viewing the collected data. Use an external tool to plot your tab counts over time.

# See also
* [Tab Counter](https://addons.mozilla.org/en-US/firefox/addon/tabcounter/): a preexisting tab-counter extension that keeps some statistics