OMERO Web Runtime
=================

OMERO.web runtime dependencies.

Mostly Python modules.

Status: DEPRECATED
------------------

This role has been replaced by the more complete
https://github.com/openmicroscopy/ansible-role-omero-web,
which in turn depends on
https://github.com/openmicroscopy/ansible-role-omero-python-deps
for functionality similar to this role.

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
