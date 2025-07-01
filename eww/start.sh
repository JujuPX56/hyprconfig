#!/bin/bash

while true; do
  if [ $(hyprctl activeworkspace -j | jq '.windows') = "0" ]; then
    if [[ $(eww active-windows) == "" ]]; then
      pkill waybar
      eww open date
      eww open time
      eww open powermenu
    fi
  else
    if [[ $(pgrep waybar) == "" ]]; then
      eww close-all
      waybar &
    fi
  fi
done
