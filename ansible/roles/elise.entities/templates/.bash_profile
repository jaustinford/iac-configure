#!/usr/bin/env bash

if [ "${MSYSTEM}" == 'MINGW64' ]; then
    COLOR_NAME_PRIMARY='red'
    COLOR_NAME_SECONDARY='white'
    COLOR_NAME_TERTIARY='lightgrey'

else
    COLOR_NAME_PRIMARY="{{ item.profile.colors.primary }}"
    COLOR_NAME_SECONDARY="{{ item.profile.colors.secondary }}"
    COLOR_NAME_TERTIARY="{{ item.profile.colors.tertiary }}"

    if [ "$(hostname)" == "{{ names.hosts.nas }}.{{ lab.domain }}" ]; then cd "/mnt/{{ names.raid }}/root"
    elif [ "$(hostname)" == "{{ names.hosts.docker00 }}.{{ lab.domain }}" ]; then cd "{{ folder_root }}"
    elif [ "$(hostname)" == "{{ names.hosts.docker01 }}.{{ lab.domain }}" ]; then cd "{{ folder_root }}"
    elif [ "$(hostname)" == "{{ names.hosts.docker02 }}.{{ lab.domain }}" ]; then cd "{{ folder_root }}"
    fi

fi

resolve_color_code() {
    color_name_query="${1}"

    bash_colors=(
        "0:white"
        "30:grey"
        "31:red"
        "32:green"
        "33:yellow"
        "34:blue"
        "35:purple"
        "36:cyan"
        "90:lightgrey"
        "91:lightred"
        "92:lightgreen"
        "93:lightyellow"
        "94:lightblue"
        "95:lightpurple"
        "96:lightcyan"
    )

    for bash_color in ${bash_colors[@]}; do
        bash_color_code="$(echo ${bash_color} | cut -d ':' -f1)"
        bash_color_name="$(echo ${bash_color} | cut -d ':' -f2)"

        if [ "${bash_color_name}" == "${color_name_query}" ]; then
            echo "${bash_color_code}"
            break

        fi

    done
}

export_ps1() {
    c_primary="${1}"
    c_secondary="${2}"
    c_tertiary="${3}"

    c_escape="\[\e["
    c_close="m\]"
    c_reset="${c_escape}0${c_close}"

    s_regular="0"
    s_bold="1"
    s_dim="2"
    s_italics="3"
    s_underline="4"

    export PS1="\n \
[ ${c_escape}${s_regular};${c_primary}${c_close}\u${c_reset} ] \
${c_escape}${s_regular};${c_secondary}${c_close}\H${c_reset} \
${c_escape}${s_regular};${c_tertiary}${c_close}\w${c_reset}\n   \
${c_escape}${s_regular};${c_primary}${c_close}\$${c_reset} "
}

alias tree="tree -aC"
alias ls="ls --color=auto"
alias grep="grep --color=auto"
alias egrep="egrep --color=auto"
alias _source="source ~/.bash_profile"

export TZ="America/Denver"

export_ps1 \
    $(resolve_color_code "${COLOR_NAME_PRIMARY}") \
    $(resolve_color_code "${COLOR_NAME_SECONDARY}") \
    $(resolve_color_code "${COLOR_NAME_TERTIARY}")
