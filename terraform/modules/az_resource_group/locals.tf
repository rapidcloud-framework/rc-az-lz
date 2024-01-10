locals {
  name     = var.name
  location = var.location
  rc_tags = {
    env     = var.env
    profile = var.profile
    author  = "rapid-cloud"
  }
}
