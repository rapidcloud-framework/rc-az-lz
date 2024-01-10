resource "azurerm_role_assignment" "main" {
  name               = local.role_assignment_name
  scope              = local.role_assignment_scope
  role_definition_id = local.role_definition_id
  principal_id       = local.principal_id
}