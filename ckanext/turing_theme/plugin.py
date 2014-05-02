import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class TuringThemePlugin(plugins.SingletonPlugin):
	'''If Turing had a copy of CKAN...

	'''
	plugins.implements(plugins.IConfigurer)
	
	def update_config(self, config):
		toolkit.add_template_directory(config, 'templates')
