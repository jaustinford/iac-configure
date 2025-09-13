#!/bin/bash

COLOR_NAME_PRIMARY="purple"
COLOR_NAME_SECONDARY="white"
COLOR_NAME_TERTIARY="lightgrey"

COLOR_CODE_ESCAPE="\033["
COLOR_CODE_RESET="${COLOR_CODE_ESCAPE}0m"

STYLE_CODE_REGULAR="0"
STYLE_CODE_BOLD="1"
STYLE_CODE_ITALICS="3"

BASH_COLORS=(
    "90:lightgrey"
    "91:lightred"
    "92:lightgreen"
    "93:lightyellow"
    "94:lightblue"
    "95:lightpurple"
    "96:lightcyan"
    "30:grey"
    "31:red"
    "32:green"
    "33:yellow"
    "34:blue"
    "35:purple"
    "36:cyan"
    "0:white"
)

resolve_color_code() {
    color_name_query="${1}"

    for bash_color in ${BASH_COLORS[@]}; do
        bash_color_code="$(echo ${bash_color} | cut -d ':' -f1)"
        bash_color_name="$(echo ${bash_color} | cut -d ':' -f2)"

        if [ "${bash_color_name}" == "${color_name_query}" ]; then
            echo "${bash_color_code}"
            break

        fi

    done
}

color_code_primary=$(resolve_color_code "${COLOR_NAME_PRIMARY}")
color_code_secondary=$(resolve_color_code "${COLOR_NAME_SECONDARY}")
color_code_tertiary=$(resolve_color_code "${COLOR_NAME_TERTIARY}")

color_concat_user="${COLOR_CODE_ESCAPE}${STYLE_CODE_ITALICS};${color_code_primary}m"
color_concat_time="${COLOR_CODE_ESCAPE}${STYLE_CODE_REGULAR};${color_code_primary}m"
color_concat_host="${COLOR_CODE_ESCAPE}${STYLE_CODE_BOLD};${color_code_secondary}m"
color_concat_cwd="${COLOR_CODE_ESCAPE}${STYLE_CODE_REGULAR};${color_code_tertiary}m"
color_concat_prompt="${COLOR_CODE_ESCAPE}${STYLE_CODE_REGULAR};${color_code_primary}m"

alias ls="ls --color=auto"
alias grep="grep --color=auto"
alias egrep="egrep --color=auto"

export TZ="America/Denver"

export PS1="\n \
[ ${color_concat_user}\u${COLOR_CODE_RESET} ] \
${color_concat_host}\H${COLOR_CODE_RESET}:\
${color_concat_cwd}\w${COLOR_CODE_RESET} \
[ ${color_concat_time}\d${COLOR_CODE_RESET} - \
${color_concat_time}\t${COLOR_CODE_RESET} ]\n   \
${color_concat_prompt}\$${COLOR_CODE_RESET} "
