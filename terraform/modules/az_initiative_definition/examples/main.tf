# data azurerm_policy_definition audit_virtual_machines {
#   display_name = "Audit virtual machines without disaster recovery configured"
# }

# module configure_asc_initiative {
#   source                  = "../"
#   initiative_name         = "configure_asc_initiative"
#   initiative_display_name = "[Security]: Configure Azure Security Center"
#   initiative_description  = "Deploys and configures Azure Security Center settings and defines exports"
#   initiative_category     = "Security Center"
#   management_group_id     = "/providers/Microsoft.Management/managementGroups/e4de106e-71f0-47e6-9741-36a034b3bdf8"
#   merge_effects           = false

#   member_definitions = [
#     data.azurerm_policy_definition.audit_virtual_machines
#   ]
# }