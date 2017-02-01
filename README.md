OMERO Web Runtime
=================

OMERO.web runtime dependencies.

Mostly Python modules.

Dependencies
------------

See `meta/main.yml`.
The dependency `omero-python-deps` is installed with the default (recommended) options.
If you wish you can set `omero_python_deps_recommended: False` to only install the minimum requirements, for instance during development.
This is not supported in production.


Role Variables
--------------

Optional variables:
- `omero_web_runtime_redis`: If `True` install redis dependencies, default `False`


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
