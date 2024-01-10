resource "azurerm_management_group_policy_assignment" "main" {
  name                 = var.policy_assignment_name
  policy_definition_id = var.policy_definition_id
  management_group_id  = var.management_group_id
}
