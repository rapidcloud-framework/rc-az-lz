resource azurerm_policy_definition def {
  name         = local.policy_name
  display_name = local.policy_name
  policy_type  = "Custom"
  mode         = local.mode

  metadata    = local.metadata
  parameters  = length(local.parameters) > 0 ? local.parameters : null
  policy_rule = local.policy_rule

  lifecycle {
    create_before_destroy = true
  }

  timeouts {
    read = "10m"
  }
}