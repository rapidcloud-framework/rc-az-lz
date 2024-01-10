
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

variable data_actions {
  type        = any
  default = []
}
variable not_data_actions {
  type        = any
  default = []
}

variable assignable_scopes {
  type        = any
  default = null
}


variable "role_assignment_name" {
  type = string
  default = ""
}

variable "role_assignment_scope" {
  type    = string
  default = ""
}

variable "role_definition_id" {
  type    = string
  default = ""
}

variable "principal_id" {
  type    = string
  default = ""
}
