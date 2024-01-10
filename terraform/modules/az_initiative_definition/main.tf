resource azurerm_policy_set_definition set {
  name         = local.initiative_name
  display_name = local.initiative_name
  policy_type  = "Custom"

  parameters = local.parameters

  policy_definition_reference {
    policy_definition_id = local.policy_definition_id
    parameter_values = local.metadata
  }

  timeouts {
    read = "10m"
  }
}