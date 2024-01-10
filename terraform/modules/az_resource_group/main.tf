resource "azurerm_resource_group" "main" {
  name     = local.name
  location = local.location
  tags     = merge(local.rc_tags, var.tags)
}
