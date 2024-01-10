resource "azurerm_log_analytics_solution" "example" {
  solution_name         = local.solution_name
  location              = local.location
  resource_group_name   = local.resource_group_name
  workspace_resource_id = data.azurerm_log_analytics_workspace.main.id
  workspace_name        = local.workspace_name

   plan {
    publisher = local.publisher
    product   = local.product
  }
}

data "azurerm_log_analytics_workspace" "main" {
  name                = local.workspace_name
  resource_group_name = local.resource_group_name
}