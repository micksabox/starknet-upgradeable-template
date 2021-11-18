%lang starknet

# These are interfaces that can be imported by other contracts for convenience.
# All of the functions in an interface must be @view or @external.

# Interface for the ModuleController.
@contract_interface
namespace IModuleController:
    func get_module_address(
        module_id : felt
    ) -> (
        address : felt
    ):
    end

    func has_write_access(
        address_attempting_to_write : felt
    ):
    end

    func appoint_new_arbiter(
        new_arbiter : felt
    ):
    end

    func set_address_for_module_id(
        module_id : felt,
        module_address : felt):
    end

    func set_write_access(
        module_id_doing_writing : felt,
        module_id_being_written_to : felt):
    end

    func set_initial_module_addresses(
        module_01_addr : felt,
        module_02_addr : felt,
        module_03_addr : felt,
        module_04_addr : felt,
        module_05_addr : felt,
        module_06_addr : felt,
        module_07_addr : felt):
    end
end