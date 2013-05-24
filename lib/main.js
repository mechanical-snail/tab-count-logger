const tabs = require("sdk/tabs");
const windows = require("sdk/windows").browserWindows;
const sqlite = require("./deps/sqlite") ;

const initDB = function initDB() {
	console.log("Initializing database for logging tab counts...");
	sqlite.connect("tabCountLog.sqlite");
	sqlite.execute("CREATE TABLE tabCountLog(timestamp TEXT PRIMARY KEY, windows INTEGER, tabs INTEGER);", {}, function(){console.log("Finished initializing database");});
}
initDB();

const DEBUG = true;

const logTabs = function logTabs() {
	if(DEBUG) console.log("Windows: " + windows.length + "; tabs: " + tabs.length);
	
	// asynchronous, so should be fast
	sqlite.execute("INSERT INTO tabCountLog(timestamp, windows, tabs) VALUES(DATETIME('now'), :windows, :tabs);", {
		windows: windows.length,
		tabs: tabs.length
	}, function(){
		if(DEBUG) console.log("Saved to database");
	});
}

// Log new counts on each relevant event.
// Firefox fires spurious events when shutting down, creating windows, or moving tabs between windows.
// There also seems to be a race condition. So these are disabled.
/*
tabs.on("open", logTabs);
tabs.on("close", logTabs);
windows.on("open", logTabs);
windows.on("close", logTabs);
*/

// In case we miss changes, occasionally log even if no events occurred.
const LOGGING_FREQUENCY = 30000 /*ms*/;
require("sdk/timers").setInterval(logTabs, LOGGING_FREQUENCY);

const widget = require("sdk/widget").Widget({
  id: "status-icon",
  label: "Tab Count Logger",
  content: "Tab Count Logger",
  width: 100,
  onClick: logTabs
});
