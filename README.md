# Powerline Kubernetes

A [Powerline](https://github.com/powerline/powerline) segment to show the current Kubernetes context.

This segment shows the Kubernetes context together with a nice looking helm. Please feel free to propose more features and give me ideas on how to improve it.

This is a "rewrite" of [powerline-kubernetes](https://github.com/so0k/powerline-kubernetes), which uses the python kubernetes package. The package is relativly slow getting the context from huge kubeconfig files. By default this package uses the `kubectl` commandline tool to determine the current context and namespace. This can be configured to use any custom command to determine the context and namespace.


## Requirements

The Kubernetes segment requires kubectl to be available in the `$PATH`, if used in the default configuration.


## Installation

Installing the Kubernetes segment can be done with `pip`:

```
$ git clone https://github.com/dellacf/powerline-k8s.git
$ pip install ./powerline-k8s
```

The Kubernetes segment uses a couple of custom highlight groups. You'll need to define those groups in your colorscheme, for example in `~/.config/powerline/colorschemes/default.json`:

```json
{
  "groups": {
    "kubernetes_cluster":         { "fg": "gray10", "bg": "darkestblue", "attrs": [] },
    "kubernetes_cluster:alert":   { "fg": "gray10", "bg": "darkestred",  "attrs": [] },
    "kubernetes_namespace":       { "fg": "gray10", "bg": "darkestblue", "attrs": [] },
    "kubernetes_namespace:alert": { "fg": "gray10", "bg": "darkred",     "attrs": [] },
    "kubernetes:divider":         { "fg": "darkblue",  "bg": "darkestblue", "attrs": [] },
    "kubernetes:divider:alert":   { "fg": "darkred",  "bg": "darkestred", "attrs": [] }
  }
}
```

Then you can activate the Kubernetes segment by adding it to your segment configuration, for example in `~/.config/powerline/themes/shell/default.json`:

```javascript
{
  "segments": {
    "left": [
      {
        "function": "powerline-k8s.kubernetes",
        "priority": 10,
        "draw_inner_divider": true,
        "after": " ",
        "args": {
          "show_kube_logo": true,
          "show_cluster": true,
          "show_namespace": true,
          "show_default_namespace": false,
          "context_cmd": "kubectl config current-context,
          "namespace_cmd": "kubectl config view --minify --output 'jsonpath={..namespace}'",
          "context_alert_regex": "^$",
          "namespace_alert_regex": "^$"
        }
      }
    ]
  }
}

```

## License

Licensed under the [MIT License](LICENSE).


## Authors

Created by [so0k](https://github.com/so0k/). Code contributions by [bokysan](https://github.com/bokysan). Rewritten by [dellacf](https://github.com/dellacf/).

