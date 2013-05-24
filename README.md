# Tab Count Logger

Tab Count Logger is a Firefox extension that periodically logs a count of open tabs/windows to an SQLite database. It was created because existing tab-counter extensions recorded only scalar statistics rather than a full history.

Currently it is hard-coded to collect a count once every 30 s.

# Usage
While the extension is installed and enabled, it will display "Tab Count Logger" in the status bar and log to an SQLite database, `tabCountLog.sqlite` in your profile directory. Clicking the text causes it to immediately record a count. To pause data collection, disable the extension.

There is no UI for viewing the collected data. Use an external tool to plot your tab counts over time.

# See also
* @@@@ Other tab count extensions