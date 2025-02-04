.. _ref_admin_config:

====================
Server configuration
====================

EdgeDB exposes a number of configuration parameters that affect its
behavior.  In this section we review the ways to change the server
configuration, as well as detail each available configuration parameter.


Configuring the server
======================

EdgeQL
------

The :eql:stmt:`configure <CONFIGURE>` command can be used to set the
configuration parameters using EdgeQL. For example:

.. code-block:: edgeql-repl

  edgedb> configure instance set listen_addresses := {'127.0.0.1', '::1'};
  CONFIGURE: OK

CLI
---

The :ref:`ref_cli_edgedb_configure` command allows modifying the system
configuration from a terminal:

.. code-block:: bash

  $ edgedb configure set listen_addresses 127.0.0.1 ::1


Available settings
==================

Below is an overview of available settings. a full reference of settings is
available at :ref:`Standard Library > Config <ref_std_cfg>`.


Connection settings
-------------------

:eql:synopsis:`listen_addresses -> multi str`
  The TCP/IP address(es) on which the server is to listen for
  connections from client applications.

:eql:synopsis:`listen_port -> int16`
  The TCP port the server listens on; defaults to ``5656``.

Resource usage
--------------

:eql:synopsis:`effective_io_concurrency -> int64`
  The number of concurrent disk I/O operations that can be
  executed simultaneously.

:eql:synopsis:`query_work_mem -> cfg::memory`
  The amount of memory used by internal query operations such as
  sorting.

:eql:synopsis:`shared_buffers -> cfg::memory`
  The amount of memory used for shared memory buffers.

Query planning
--------------

:eql:synopsis:`default_statistics_target -> int64`
  The default data statistics target for the planner.

:eql:synopsis:`effective_cache_size -> cfg::memory`
  An estimate of the effective size of the disk
  cache available to a single query.

Client connections
------------------

:eql:synopsis:`session_idle_timeout -> std::duration`
  How long client connections can stay inactive before being closed by the
  server. Defaults to 60 seconds; set to ``<duration>'0'`` to disable the
  mechanism.

:eql:synopsis:`session_idle_transaction_timeout -> std::duration`
  How long client connections can stay inactive
  while in a transaction. Defaults to 10 seconds; set to ``<duration>'0'`` to
  disable the mechanism.

:eql:synopsis:`query_execution_timeout -> std::duration`
  How long an individual query can run before being aborted. A value of
  ``<duration>'0'`` disables the mechanism; it is disabled by default.
