# vim:fileencoding=utf-8:noet:tabstop=4:softtabstop=4:shiftwidth=4:

import os
import re
import subprocess
from powerline.theme import requires_segment_info
from powerline.segments import Segment, with_docstring

_KUBERNETES = u'\U00002388 '

@requires_segment_info
class KubernetesSegment(Segment):

	def is_alert(self, context, namespace):
		context_match = re.search(self.context_alert_regex, context)
		if context_match:
			return True

		namespace_match = re.search(self.namespace_alert_regex, namespace)
		if namespace_match:
			return True
		
		return False


	def build_segments(self, context, namespace):
		alert = self.is_alert(context, namespace)

		segments = []

		divider = 'kubernetes:divider:alert' if alert else 'kubernetes:divider'
		if self.show_cluster:
			color = 'kubernetes_cluster:alert' if alert else 'kubernetes_cluster'

			if self.show_kube_logo:
				context = _KUBERNETES + context

			segments.append({
				'contents': context,
				'highlight_groups': [color],
				'divider_highlight_group': divider
			})

		if self.show_namespace:
			color = 'kubernetes_namespace:alert' if alert else 'kubernetes_namespace'

			if namespace != 'default' or self.show_default_namespace:
				if not self.show_cluster and self.show_kube_logo:
					namespace = _KUBERNETES + namespace

				segments.append({
					'contents': namespace,
					'highlight_groups': [color],
					'divider_highlight_group': divider
				})

		return segments

	def execute_cmd(self, cmd):
		self.pl.debug('Executing command: \'%s\'', cmd)

		try:
			cmd_process = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			cmd_return_code = cmd_process.wait()
			cmd_output = cmd_process.communicate()
			if cmd_return_code != 0:
				cmd_stderr = cmd_output[1].decode('Utf-8')
				self.pl.error('Command \'%s\' returned non-zero return code: \n%s', cmd, cmd_stderr)
				return
			cmd_stdout = cmd_output[0].decode('Utf-8').rstrip()
		except Exception as e:
			self.pl.error(e)
			return

		return cmd_stdout

	def __init__(self):
		self.pl = None
		self.show_kube_logo = None
		self.show_cluster = None
		self.show_namespace = None
		self.show_default_namespace = None
		self.context_cmd = None
		self.namespace_cmd = None
		self.context_alert_regex = None
		self.namespace_alert_regex = None

	def __call__(
			self,
			pl,
			show_kube_logo=True,
			show_cluster=True,
			show_namespace=True,
			show_default_namespace=False,
			context_cmd = 'kubectl config current-context',
			namespace_cmd = 'kubectl config view --minify --output \'jsonpath={..namespace}\'',
			context_alert_regex = "^$",
			namespace_alert_regex = "^$",
			**kwargs
		):
		pl.debug('Running powerline-kubernetes')
		self.pl = pl
		self.show_kube_logo = show_kube_logo
		self.show_cluster = show_cluster
		self.show_namespace = show_namespace
		self.show_default_namespace = show_default_namespace
		self.context_cmd = context_cmd
		self.namespace_cmd = namespace_cmd
		self.context_alert_regex = context_alert_regex
		self.namespace_alert_regex = namespace_alert_regex
		
		context = self.execute_cmd(self.context_cmd)
		namespace = self.execute_cmd(self.namespace_cmd)

		return self.build_segments(context, namespace)

kubernetes = with_docstring(KubernetesSegment(),
'''Return the current context.

It will show the current context in config.
It requires kubectl to be available in the $PATH.

Divider highlight group used: ``kubernetes:divider``
and ``kubernetes:divider:alert``

Highlight groups used: ``kubernetes_cluster``,
``kubernetes_cluster:alert``, ``kubernetes_namespace``,
and ``kubernetes_namespace:alert``, .
''')
