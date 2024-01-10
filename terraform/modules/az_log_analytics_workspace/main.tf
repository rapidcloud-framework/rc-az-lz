resource "azurerm_log_analytics_workspace" "main" {
  name                = local.name
  location            = local.location
  resource_group_name = local.resource_group_name
  sku                 = local.sku
  retention_in_days   = local.retention_in_days
}
