## Architecture
Inspired/copied from DOPE wars [architecture](https://github.com/dopedao/RYO/blob/main/system_architecture.md).

### Contract Upgradeability
There is an account in the system called the `Arbiter`. The Arbiter is the most powerful actor in the system, with the ability to modify the `Controller` (adding/replacing modules).

### Controller
The `Controller` contains references to the various modules used in the system. During implementation, the various interoperable modules must retrieve the dynamic address of the module contract from the controller. For example, the `Game` module must retrieve the current address of the `Resource` module by first querying the controller, for example: `get_module_contract(module_id)`.

### Modules
...