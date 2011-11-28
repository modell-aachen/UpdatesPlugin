# ---+ Extensions
# ---++ UpdatesPlugin
# This is the configuration used by the <b>UpdatesPlugin</b>.

# **URL**
# The source URL where to get the latest version of extensions. The URL must point to a page
# that generates a list in the same format as the list generated by
# http://foswiki.org/Extensions/UpdatesPluginReport
$Foswiki::cfg{Plugins}{UpdatesPlugin}{ReportUrl} = "http://foswiki.org/Extensions/UpdatesPluginReport";

# **URL**
# A proxy URL that is normally used to obtain the update report. This is normally the URL of a REST
# handler on the local site. Note: don't forget to remove 'rest' from the {AuthScripts} setting,
# or this won't work. You can set this URL to the empty path, which will force the plugin to refer
# back to Foswiki.org for every update check. Otherwise the response from Foswiki.org is cached
# on this server.
$Foswiki::cfg{Plugins}{UpdatesPlugin}{ProxyUrl} = '$Foswiki::cfg{ScriptUrlPath}/rest$Foswiki::cfg{ScriptSuffix}/UpdatesPlugin/report';

# **NUMBER**
# Number of seconds to cache the update report for extensions. Default is 24 hours.
$Foswiki::cfg{Plugins}{UpdatesPlugin}{ProxyCacheTimeout} = 86400;

# **URL**
# The URL of the 'configure' program used to install extensions on your Foswiki.
$Foswiki::cfg{Plugins}{UpdatesPlugin}{ConfigureUrl} = '$Foswiki::cfg{ScriptUrlPath}/configure$Foswiki::cfg{ScriptSuffix}';

1;

