from volatility3.plugins import mac
import volatility3.framework
from volatility3.framework import contexts
from volatility3 import framework

volatility3.framework.require_interface_version(2, 0, 0)

ctx = contexts.Context()
failures = framework.import_files(volatility3.plugins, True)

# volatility3.plugins.__path__ = <new_plugin_path> + constants.PLUGINS_PATH
pluginList = framework.list_plugins()

print(pluginList)

