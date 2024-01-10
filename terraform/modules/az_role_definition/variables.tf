
variable "role_name" {
  type = string
  default = ""
}

variable "role_scope" {
  type    = string
  default = ""
}

variable actions {
  type        = any
  default = []
}
variable no_actions {
  type        = any
  default = []
}

variable assignable_scopes {
  type        = any
  default = null
}