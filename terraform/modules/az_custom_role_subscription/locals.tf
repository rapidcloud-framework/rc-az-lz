locals {
  role_name = var.role_name
  role_scope = var.assignable_scopes[0] #First assignment scopes
  actions = var.actions
  no_actions = var.no_actions
  data_actions = var.data_actions
  not_data_actions = var.not_data_actions
  assignable_scopes = var.assignable_scopes
  role_assignment_name = var.role_assignment_name
  role_assignment_scope = var.assignable_scopes[0] #First assignment scopes
  role_definition_id = azurerm_role_definition.main.role_definition_id
  principal_id = var.principal_id
}