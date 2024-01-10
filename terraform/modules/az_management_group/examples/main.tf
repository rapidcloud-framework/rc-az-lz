module "management_group_main" {
    source = "../"
    management_group_name = "Landing Zone"
    isFirstLevelManagementGroup = true
}

module "management_group_custom" {
    source = "../"
    management_group_name = "Marketing"
    isFirstLevelManagementGroup = false
    parent_management_group_id = module.management_group_main.main_management_group_id
}