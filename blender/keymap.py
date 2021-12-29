keyconfig_version = (3, 0, 42)
keyconfig_data = \
[("3D View",
  {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
  {"items":
   [("view3d.cursor3d", {"type": 'LEFTMOUSE', "value": 'CLICK'}, None),
    ("view3d.localview", {"type": 'NUMPAD_SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'MOUSESMARTZOOM', "value": 'ANY'}, None),
    ("view3d.localview_remove_from", {"type": 'M', "value": 'PRESS'}, None),
    ("view3d.rotate", {"type": 'MOUSEROTATE', "value": 'ANY'}, None),
    ("view3d.rotate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
    ("view3d.move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
    ("view3d.rotate", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
    ("view3d.zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.dolly", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ],
      },
     ),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
    ("view3d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
    ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("view3d.zoom",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'EQUAL', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELINMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELOUTMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'EQUAL', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'MINUS', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.view_center_camera", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_center_lock", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS'},
     {"properties":
      [("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'C', "value": 'PRESS', "shift": True},
     {"properties":
      [("center", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_view_pie'),
       ],
      },
     ),
    ("view3d.navigate", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "shift": True}, None),
    ("view3d.navigate", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "shift": True}, None),
    ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_2', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITDOWN'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_4', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITLEFT'),
       ],
      },
     ),
    ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS'}, None),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_6', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_8', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITUP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANDOWN'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANLEFT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANRIGHT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANUP'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_9', "value": 'PRESS'},
     {"properties":
      [("angle", 3.1415927),
       ("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'NORTH', "alt": True},
     {"properties":
      [("type", 'TOP'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'SOUTH', "alt": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'EAST', "alt": True},
     {"properties":
      [("type", 'RIGHT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'EVT_TWEAK_M', "value": 'WEST', "alt": True},
     {"properties":
      [("type", 'LEFT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_center_pick", {"type": 'MIDDLEMOUSE', "value": 'CLICK', "alt": True}, None),
    ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
    ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
    ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("deselect_all", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("toggle", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("center", True),
       ("object", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("view3d.select_lasso",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("view3d.select_lasso",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("view3d.select_circle", {"type": 'C', "value": 'PRESS'}, None),
    ("view3d.clip_border", {"type": 'B', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("view3d.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.camera_to_view", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.object_as_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("transform.translate", {"type": 'EVT_TWEAK_R', "value": 'ANY'}, None),
    ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
    ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
    ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
    ("transform.tosphere", {"type": 'S', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("transform.shear", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("transform.bend", {"type": 'W', "value": 'PRESS', "shift": True}, None),
    ("transform.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("object.transform_axis_target", {"type": 'T', "value": 'PRESS', "shift": True}, None),
    ("transform.skin_resize", {"type": 'A', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'TAB', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'tool_settings.use_snap'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_PT_snapping'),
       ("keep_open", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_snap_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_pivot_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'COMMA', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_orientations_pie'),
       ],
      },
     ),
    ("view3d.toggle_shading",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("type", 'WIREFRAME'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'Z', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_shading_pie'),
       ],
      },
     ),
    ("view3d.toggle_xray", {"type": 'Z', "value": 'PRESS', "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ],
   },
  ),
 ("Object Mode",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("machin3.focus",
     {"type": 'F', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("method", 'LOCAL_VIEW'),
       ("invert", True),
       ],
      },
     ),
    ("machin3.focus",
     {"type": 'F', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("method", 'LOCAL_VIEW'),
       ("invert", False),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'O', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_proportional_editing_falloff_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("data_path", 'tool_settings.use_proportional_edit_objects'),
       ],
      },
     ),
    ("object.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'SELECT'),
       ],
      },
     ),
    ("object.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("object.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("object.select_all",
     {"type": 'A', "value": 'DOUBLE_CLICK'},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("object.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("object.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("object.select_linked", {"type": 'L', "value": 'PRESS', "shift": True}, None),
    ("object.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
    ("object.select_hierarchy",
     {"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},
     {"properties":
      [("direction", 'PARENT'),
       ("extend", False),
       ],
      },
     ),
    ("object.select_hierarchy",
     {"type": 'LEFT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("direction", 'PARENT'),
       ("extend", True),
       ],
      },
     ),
    ("object.select_hierarchy",
     {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},
     {"properties":
      [("direction", 'CHILD'),
       ("extend", False),
       ],
      },
     ),
    ("object.select_hierarchy",
     {"type": 'RIGHT_BRACKET', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("direction", 'CHILD'),
       ("extend", True),
       ],
      },
     ),
    ("object.parent_set", {"type": 'P', "value": 'PRESS', "ctrl": True}, None),
    ("object.parent_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
    ("object.location_clear",
     {"type": 'G', "value": 'PRESS', "alt": True},
     {"properties":
      [("clear_delta", False),
       ],
      },
     ),
    ("object.rotation_clear",
     {"type": 'R', "value": 'PRESS', "alt": True},
     {"properties":
      [("clear_delta", False),
       ],
      },
     ),
    ("object.scale_clear",
     {"type": 'S', "value": 'PRESS', "alt": True},
     {"properties":
      [("clear_delta", False),
       ],
      },
     ),
    ("object.delete",
     {"type": 'X', "value": 'PRESS'},
     {"properties":
      [("use_global", False),
       ],
      },
     ),
    ("object.delete",
     {"type": 'X', "value": 'PRESS', "shift": True},
     {"properties":
      [("use_global", True),
       ],
      },
     ),
    ("object.delete",
     {"type": 'DEL', "value": 'PRESS'},
     {"properties":
      [("use_global", False),
       ("confirm", False),
       ],
      },
     ),
    ("object.delete",
     {"type": 'DEL', "value": 'PRESS', "shift": True},
     {"properties":
      [("use_global", True),
       ("confirm", False),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_add'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_object_apply'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'L', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_MT_make_links'),
       ],
      },
     ),
    ("object.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("object.duplicate_move_linked", {"type": 'D', "value": 'PRESS', "alt": True}, None),
    ("object.join", {"type": 'J', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'PERIOD', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'tool_settings.use_transform_data_origin'),
       ],
      },
     ),
    ("anim.keyframe_insert_menu", {"type": 'I', "value": 'PRESS'}, None),
    ("anim.keyframe_delete_v3d", {"type": 'I', "value": 'PRESS', "alt": True}, None),
    ("anim.keying_set_active_set", {"type": 'I', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("collection.create", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
    ("collection.objects_remove", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("collection.objects_remove_all", {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("collection.objects_add_active", {"type": 'G', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("collection.objects_remove_active", {"type": 'G', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("object.subdivision_set",
     {"type": 'ZERO', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 0),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'ONE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 1),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'TWO', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 2),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'THREE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 3),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'FOUR', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 4),
       ("relative", False),
       ],
      },
     ),
    ("object.subdivision_set",
     {"type": 'FIVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("level", 5),
       ("relative", False),
       ],
      },
     ),
    ("object.move_to_collection", {"type": 'M', "value": 'PRESS'}, None),
    ("object.link_to_collection", {"type": 'M', "value": 'PRESS', "shift": True}, None),
    ("object.hide_view_clear", {"type": 'H', "value": 'PRESS', "alt": True}, None),
    ("object.hide_view_set",
     {"type": 'H', "value": 'PRESS'},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("object.hide_view_set",
     {"type": 'H', "value": 'PRESS', "shift": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("object.hide_collection", {"type": 'H', "value": 'PRESS', "ctrl": True}, None),
    ("object.hide_collection",
     {"type": 'ONE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 1),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'TWO', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 2),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'THREE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 3),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'FOUR', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 4),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'FIVE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 5),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'SIX', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 6),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'SEVEN', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 7),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'EIGHT', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 8),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'NINE', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 9),
       ],
      },
     ),
    ("object.hide_collection",
     {"type": 'ZERO', "value": 'PRESS', "any": True},
     {"properties":
      [("collection_index", 10),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'W', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_object_context_menu'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'APP', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_object_context_menu'),
       ],
      },
     ),
    ("object.modifier_add",
     {"type": 'M', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'MIRROR'),
       ],
      },
     ),
    ],
   },
  ),
 ("Screen",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("pillar.browser", {"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("screen.animation_step", {"type": 'TIMER0', "value": 'ANY', "any": True}, None),
    ("screen.region_blend", {"type": 'TIMERREGION', "value": 'ANY', "any": True}, None),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_DOWN', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_UP', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.region_quadview", {"type": 'Q', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("screen.repeat_last", {"type": 'R', "value": 'PRESS', "shift": True, "repeat": True}, None),
    ("file.execute", {"type": 'RET', "value": 'PRESS'}, None),
    ("file.execute", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
    ("file.cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("asset.catalog_undo", {"type": 'Z', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("asset.catalog_redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
    ("ed.undo", {"type": 'Z', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("ed.redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
    ("render.render",
     {"type": 'F12', "value": 'PRESS'},
     {"properties":
      [("use_viewport", True),
       ],
      },
     ),
    ("render.render",
     {"type": 'F12', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("animation", True),
       ("use_viewport", True),
       ],
      },
     ),
    ("render.view_cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("render.view_show", {"type": 'F11', "value": 'PRESS'}, None),
    ("render.play_rendered_anim", {"type": 'F11', "value": 'PRESS', "ctrl": True}, None),
    ("screen.screen_full_area", {"type": 'SPACE', "value": 'PRESS', "ctrl": True}, None),
    ("screen.screen_full_area",
     {"type": 'SPACE', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("use_hide_panels", True),
       ],
      },
     ),
    ("screen.redo_last", {"type": 'F9', "value": 'PRESS'}, None),
    ("screen.userpref_show", {"type": 'X', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True, "repeat": True}, None),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
