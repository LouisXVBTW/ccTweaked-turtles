
#************************************************************************
#
# blender python script for generating a voxelized mesh.
# be sure cycles renderer is selected before running the script.
#
#************************************************************************

import bpy

voxelSize  = 0.1
voxelScale = 0.9

widthGrid = 8
heightGrid = 8
depthGrid = 6

lookup = [ # 216 entries 
  { 'x':     5, 'y':     0, 'z':     5 }, # voxel 0
  { 'x':     6, 'y':     8, 'z':     4 }, # voxel 1
  { 'x':     5, 'y':     8, 'z':     4 }, # voxel 2
  { 'x':     4, 'y':     8, 'z':     4 }, # voxel 3
  { 'x':     3, 'y':     8, 'z':     4 }, # voxel 4
  { 'x':     2, 'y':     8, 'z':     4 }, # voxel 5
  { 'x':     1, 'y':     8, 'z':     4 }, # voxel 6
  { 'x':     7, 'y':     7, 'z':     4 }, # voxel 7
  { 'x':     6, 'y':     0, 'z':     5 }, # voxel 8
  { 'x':     7, 'y':     0, 'z':     5 }, # voxel 9
  { 'x':     0, 'y':     7, 'z':     4 }, # voxel 10
  { 'x':     7, 'y':     6, 'z':     4 }, # voxel 11
  { 'x':     0, 'y':     6, 'z':     4 }, # voxel 12
  { 'x':     8, 'y':     5, 'z':     4 }, # voxel 13
  { 'x':     5, 'y':     1, 'z':     5 }, # voxel 14
  { 'x':     6, 'y':     1, 'z':     5 }, # voxel 15
  { 'x':     0, 'y':     5, 'z':     4 }, # voxel 16
  { 'x':     8, 'y':     4, 'z':     4 }, # voxel 17
  { 'x':     7, 'y':     1, 'z':     5 }, # voxel 18
  { 'x':     1, 'y':     2, 'z':     5 }, # voxel 19
  { 'x':     0, 'y':     4, 'z':     4 }, # voxel 20
  { 'x':     8, 'y':     3, 'z':     4 }, # voxel 21
  { 'x':     2, 'y':     2, 'z':     5 }, # voxel 22
  { 'x':     3, 'y':     2, 'z':     5 }, # voxel 23
  { 'x':     4, 'y':     2, 'z':     5 }, # voxel 24
  { 'x':     5, 'y':     2, 'z':     5 }, # voxel 25
  { 'x':     6, 'y':     2, 'z':     5 }, # voxel 26
  { 'x':     7, 'y':     2, 'z':     5 }, # voxel 27
  { 'x':     0, 'y':     3, 'z':     4 }, # voxel 28
  { 'x':     8, 'y':     2, 'z':     4 }, # voxel 29
  { 'x':     0, 'y':     3, 'z':     5 }, # voxel 30
  { 'x':     7, 'y':     3, 'z':     5 }, # voxel 31
  { 'x':     0, 'y':     4, 'z':     5 }, # voxel 32
  { 'x':     4, 'y':     2, 'z':     4 }, # voxel 33
  { 'x':     7, 'y':     4, 'z':     5 }, # voxel 34
  { 'x':     0, 'y':     5, 'z':     5 }, # voxel 35
  { 'x':     1, 'y':     2, 'z':     4 }, # voxel 36
  { 'x':     8, 'y':     1, 'z':     4 }, # voxel 37
  { 'x':     7, 'y':     5, 'z':     5 }, # voxel 38
  { 'x':     6, 'y':     1, 'z':     4 }, # voxel 39
  { 'x':     5, 'y':     1, 'z':     4 }, # voxel 40
  { 'x':     3, 'y':     1, 'z':     4 }, # voxel 41
  { 'x':     2, 'y':     1, 'z':     4 }, # voxel 42
  { 'x':     8, 'y':     0, 'z':     4 }, # voxel 43
  { 'x':     7, 'y':     0, 'z':     4 }, # voxel 44
  { 'x':     6, 'y':     0, 'z':     4 }, # voxel 45
  { 'x':     6, 'y':     8, 'z':     3 }, # voxel 46
  { 'x':     5, 'y':     8, 'z':     3 }, # voxel 47
  { 'x':     4, 'y':     8, 'z':     3 }, # voxel 48
  { 'x':     3, 'y':     8, 'z':     3 }, # voxel 49
  { 'x':     2, 'y':     8, 'z':     3 }, # voxel 50
  { 'x':     1, 'y':     8, 'z':     3 }, # voxel 51
  { 'x':     7, 'y':     7, 'z':     3 }, # voxel 52
  { 'x':     0, 'y':     6, 'z':     5 }, # voxel 53
  { 'x':     7, 'y':     6, 'z':     5 }, # voxel 54
  { 'x':     0, 'y':     7, 'z':     3 }, # voxel 55
  { 'x':     7, 'y':     6, 'z':     3 }, # voxel 56
  { 'x':     0, 'y':     6, 'z':     3 }, # voxel 57
  { 'x':     8, 'y':     5, 'z':     3 }, # voxel 58
  { 'x':     0, 'y':     7, 'z':     5 }, # voxel 59
  { 'x':     7, 'y':     7, 'z':     5 }, # voxel 60
  { 'x':     0, 'y':     5, 'z':     3 }, # voxel 61
  { 'x':     8, 'y':     4, 'z':     3 }, # voxel 62
  { 'x':     1, 'y':     8, 'z':     5 }, # voxel 63
  { 'x':     2, 'y':     8, 'z':     5 }, # voxel 64
  { 'x':     0, 'y':     4, 'z':     3 }, # voxel 65
  { 'x':     8, 'y':     3, 'z':     3 }, # voxel 66
  { 'x':     3, 'y':     8, 'z':     5 }, # voxel 67
  { 'x':     4, 'y':     8, 'z':     5 }, # voxel 68
  { 'x':     4, 'y':     3, 'z':     3 }, # voxel 69
  { 'x':     5, 'y':     8, 'z':     5 }, # voxel 70
  { 'x':     6, 'y':     8, 'z':     5 }, # voxel 71
  { 'x':     0, 'y':     3, 'z':     3 }, # voxel 72
  { 'x':     8, 'y':     2, 'z':     3 }, # voxel 73
  { 'x':     1, 'y':     3, 'z':     6 }, # voxel 74
  { 'x':     6, 'y':     2, 'z':     3 }, # voxel 75
  { 'x':     5, 'y':     2, 'z':     3 }, # voxel 76
  { 'x':     3, 'y':     2, 'z':     3 }, # voxel 77
  { 'x':     2, 'y':     3, 'z':     6 }, # voxel 78
  { 'x':     1, 'y':     2, 'z':     3 }, # voxel 79
  { 'x':     8, 'y':     1, 'z':     3 }, # voxel 80
  { 'x':     7, 'y':     1, 'z':     3 }, # voxel 81
  { 'x':     3, 'y':     1, 'z':     3 }, # voxel 82
  { 'x':     2, 'y':     1, 'z':     3 }, # voxel 83
  { 'x':     8, 'y':     0, 'z':     3 }, # voxel 84
  { 'x':     7, 'y':     0, 'z':     3 }, # voxel 85
  { 'x':     6, 'y':     8, 'z':     2 }, # voxel 86
  { 'x':     5, 'y':     8, 'z':     2 }, # voxel 87
  { 'x':     4, 'y':     8, 'z':     2 }, # voxel 88
  { 'x':     3, 'y':     8, 'z':     2 }, # voxel 89
  { 'x':     2, 'y':     8, 'z':     2 }, # voxel 90
  { 'x':     1, 'y':     8, 'z':     2 }, # voxel 91
  { 'x':     7, 'y':     7, 'z':     2 }, # voxel 92
  { 'x':     3, 'y':     3, 'z':     6 }, # voxel 93
  { 'x':     4, 'y':     3, 'z':     6 }, # voxel 94
  { 'x':     0, 'y':     7, 'z':     2 }, # voxel 95
  { 'x':     7, 'y':     6, 'z':     2 }, # voxel 96
  { 'x':     0, 'y':     6, 'z':     2 }, # voxel 97
  { 'x':     8, 'y':     5, 'z':     2 }, # voxel 98
  { 'x':     5, 'y':     3, 'z':     6 }, # voxel 99
  { 'x':     6, 'y':     3, 'z':     6 }, # voxel 100
  { 'x':     0, 'y':     5, 'z':     2 }, # voxel 101
  { 'x':     8, 'y':     4, 'z':     2 }, # voxel 102
  { 'x':     7, 'y':     3, 'z':     6 }, # voxel 103
  { 'x':     1, 'y':     4, 'z':     6 }, # voxel 104
  { 'x':     0, 'y':     4, 'z':     2 }, # voxel 105
  { 'x':     8, 'y':     3, 'z':     2 }, # voxel 106
  { 'x':     2, 'y':     4, 'z':     6 }, # voxel 107
  { 'x':     3, 'y':     4, 'z':     6 }, # voxel 108
  { 'x':     4, 'y':     4, 'z':     6 }, # voxel 109
  { 'x':     5, 'y':     4, 'z':     6 }, # voxel 110
  { 'x':     6, 'y':     4, 'z':     6 }, # voxel 111
  { 'x':     7, 'y':     4, 'z':     6 }, # voxel 112
  { 'x':     0, 'y':     3, 'z':     2 }, # voxel 113
  { 'x':     8, 'y':     2, 'z':     2 }, # voxel 114
  { 'x':     1, 'y':     5, 'z':     6 }, # voxel 115
  { 'x':     2, 'y':     5, 'z':     6 }, # voxel 116
  { 'x':     3, 'y':     5, 'z':     6 }, # voxel 117
  { 'x':     4, 'y':     2, 'z':     2 }, # voxel 118
  { 'x':     4, 'y':     5, 'z':     6 }, # voxel 119
  { 'x':     5, 'y':     5, 'z':     6 }, # voxel 120
  { 'x':     1, 'y':     2, 'z':     2 }, # voxel 121
  { 'x':     8, 'y':     1, 'z':     2 }, # voxel 122
  { 'x':     6, 'y':     5, 'z':     6 }, # voxel 123
  { 'x':     6, 'y':     1, 'z':     2 }, # voxel 124
  { 'x':     5, 'y':     1, 'z':     2 }, # voxel 125
  { 'x':     3, 'y':     1, 'z':     2 }, # voxel 126
  { 'x':     2, 'y':     1, 'z':     2 }, # voxel 127
  { 'x':     8, 'y':     0, 'z':     2 }, # voxel 128
  { 'x':     7, 'y':     0, 'z':     2 }, # voxel 129
  { 'x':     6, 'y':     0, 'z':     2 }, # voxel 130
  { 'x':     6, 'y':     8, 'z':     1 }, # voxel 131
  { 'x':     5, 'y':     8, 'z':     1 }, # voxel 132
  { 'x':     4, 'y':     8, 'z':     1 }, # voxel 133
  { 'x':     3, 'y':     8, 'z':     1 }, # voxel 134
  { 'x':     2, 'y':     8, 'z':     1 }, # voxel 135
  { 'x':     1, 'y':     8, 'z':     1 }, # voxel 136
  { 'x':     7, 'y':     7, 'z':     1 }, # voxel 137
  { 'x':     7, 'y':     5, 'z':     6 }, # voxel 138
  { 'x':     1, 'y':     6, 'z':     6 }, # voxel 139
  { 'x':     2, 'y':     6, 'z':     6 }, # voxel 140
  { 'x':     3, 'y':     6, 'z':     6 }, # voxel 141
  { 'x':     0, 'y':     7, 'z':     1 }, # voxel 142
  { 'x':     7, 'y':     6, 'z':     1 }, # voxel 143
  { 'x':     4, 'y':     6, 'z':     6 }, # voxel 144
  { 'x':     5, 'y':     6, 'z':     6 }, # voxel 145
  { 'x':     0, 'y':     6, 'z':     1 }, # voxel 146
  { 'x':     7, 'y':     5, 'z':     1 }, # voxel 147
  { 'x':     6, 'y':     6, 'z':     6 }, # voxel 148
  { 'x':     7, 'y':     6, 'z':     6 }, # voxel 149
  { 'x':     0, 'y':     5, 'z':     1 }, # voxel 150
  { 'x':     7, 'y':     4, 'z':     1 }, # voxel 151
  { 'x':     1, 'y':     7, 'z':     6 }, # voxel 152
  { 'x':     2, 'y':     7, 'z':     6 }, # voxel 153
  { 'x':     3, 'y':     7, 'z':     6 }, # voxel 154
  { 'x':     4, 'y':     7, 'z':     6 }, # voxel 155
  { 'x':     0, 'y':     4, 'z':     1 }, # voxel 156
  { 'x':     7, 'y':     3, 'z':     1 }, # voxel 157
  { 'x':     5, 'y':     7, 'z':     6 }, # voxel 158
  { 'x':     6, 'y':     7, 'z':     6 }, # voxel 159
  { 'x':     2, 'y':     8, 'z':     6 }, # voxel 160
  { 'x':     3, 'y':     8, 'z':     6 }, # voxel 161
  { 'x':     4, 'y':     8, 'z':     6 }, # voxel 162
  { 'x':     5, 'y':     8, 'z':     6 }, # voxel 163
  { 'x':     0, 'y':     3, 'z':     1 }, # voxel 164
  { 'x':     7, 'y':     2, 'z':     1 }, # voxel 165
  { 'x':     6, 'y':     2, 'z':     1 }, # voxel 166
  { 'x':     5, 'y':     2, 'z':     1 }, # voxel 167
  { 'x':     4, 'y':     2, 'z':     1 }, # voxel 168
  { 'x':     3, 'y':     2, 'z':     1 }, # voxel 169
  { 'x':     2, 'y':     2, 'z':     1 }, # voxel 170
  { 'x':     1, 'y':     2, 'z':     1 }, # voxel 171
  { 'x':     7, 'y':     1, 'z':     1 }, # voxel 172
  { 'x':     6, 'y':     1, 'z':     1 }, # voxel 173
  { 'x':     5, 'y':     1, 'z':     1 }, # voxel 174
  { 'x':     7, 'y':     0, 'z':     1 }, # voxel 175
  { 'x':     6, 'y':     0, 'z':     1 }, # voxel 176
  { 'x':     5, 'y':     0, 'z':     1 }, # voxel 177
  { 'x':     5, 'y':     8, 'z':     0 }, # voxel 178
  { 'x':     4, 'y':     8, 'z':     0 }, # voxel 179
  { 'x':     3, 'y':     8, 'z':     0 }, # voxel 180
  { 'x':     2, 'y':     8, 'z':     0 }, # voxel 181
  { 'x':     6, 'y':     7, 'z':     0 }, # voxel 182
  { 'x':     5, 'y':     7, 'z':     0 }, # voxel 183
  { 'x':     4, 'y':     7, 'z':     0 }, # voxel 184
  { 'x':     3, 'y':     7, 'z':     0 }, # voxel 185
  { 'x':     2, 'y':     7, 'z':     0 }, # voxel 186
  { 'x':     1, 'y':     7, 'z':     0 }, # voxel 187
  { 'x':     7, 'y':     6, 'z':     0 }, # voxel 188
  { 'x':     6, 'y':     6, 'z':     0 }, # voxel 189
  { 'x':     5, 'y':     6, 'z':     0 }, # voxel 190
  { 'x':     4, 'y':     6, 'z':     0 }, # voxel 191
  { 'x':     3, 'y':     6, 'z':     0 }, # voxel 192
  { 'x':     2, 'y':     6, 'z':     0 }, # voxel 193
  { 'x':     1, 'y':     6, 'z':     0 }, # voxel 194
  { 'x':     7, 'y':     5, 'z':     0 }, # voxel 195
  { 'x':     6, 'y':     5, 'z':     0 }, # voxel 196
  { 'x':     5, 'y':     5, 'z':     0 }, # voxel 197
  { 'x':     4, 'y':     5, 'z':     0 }, # voxel 198
  { 'x':     3, 'y':     5, 'z':     0 }, # voxel 199
  { 'x':     2, 'y':     5, 'z':     0 }, # voxel 200
  { 'x':     1, 'y':     5, 'z':     0 }, # voxel 201
  { 'x':     7, 'y':     4, 'z':     0 }, # voxel 202
  { 'x':     6, 'y':     4, 'z':     0 }, # voxel 203
  { 'x':     5, 'y':     4, 'z':     0 }, # voxel 204
  { 'x':     4, 'y':     4, 'z':     0 }, # voxel 205
  { 'x':     3, 'y':     4, 'z':     0 }, # voxel 206
  { 'x':     2, 'y':     4, 'z':     0 }, # voxel 207
  { 'x':     1, 'y':     4, 'z':     0 }, # voxel 208
  { 'x':     7, 'y':     3, 'z':     0 }, # voxel 209
  { 'x':     6, 'y':     3, 'z':     0 }, # voxel 210
  { 'x':     5, 'y':     3, 'z':     0 }, # voxel 211
  { 'x':     4, 'y':     3, 'z':     0 }, # voxel 212
  { 'x':     3, 'y':     3, 'z':     0 }, # voxel 213
  { 'x':     2, 'y':     3, 'z':     0 }, # voxel 214
  { 'x':     1, 'y':     3, 'z':     0 }  # voxel 215
]







#//////////////////////////////////////////////////////////////////////////
#
#//////////////////////////////////////////////////////////////////////////

def tohex(r,g,b):
    hexchars = "0123456789ABCDEF"
    return "#" + hexchars[ int( r / 16 ) ] + hexchars[ int( r % 16 ) ] + hexchars[ int( g / 16 ) ] + hexchars[ int( g % 16 ) ] + hexchars[ int( b / 16 ) ] + hexchars[ int( b % 16 ) ]


#//////////////////////////////////////////////////////////////////////////
#
#//////////////////////////////////////////////////////////////////////////

def nullifyScene():

    candidate_list = [material for material in bpy.data.materials if material.name[:1] == "#"]

    for a in range(0,len(candidate_list)):
            bpy.data.materials.remove( candidate_list[ a ] )


    if 'container_voxels' in bpy.data.objects:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects['container_voxels']
        bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')
        bpy.data.objects['container_voxels'].select = True
        bpy.ops.object.delete() 

    bpy.context.scene.update()


#//////////////////////////////////////////////////////////////////////////
#
#//////////////////////////////////////////////////////////////////////////

def addVoxels( empty ):
    global voxelScale, voxelSize, voxelScale, lookup, pallette, widthGrid, heightGrid, depthGrid

    offsetX = - widthGrid / 2.0
    offsetY = - heightGrid / 2.0
    offsetZ = - depthGrid / 2.0
    
    for a in range( 0, len( lookup ) ):

        x = ( offsetX + lookup[ a ]['x'] ) * voxelSize
        y = ( offsetY + lookup[ a ]['y'] ) * voxelSize
        z = ( offsetZ + lookup[ a ]['z'] ) * voxelSize

        bpy.ops.mesh.primitive_cube_add( location = ( x, z, y ) )
        bpy.context.object.name = 'voxel'
        bpy.context.object.dimensions = ( voxelSize * voxelScale, voxelSize * voxelScale, voxelSize * voxelScale )

        name = 'voxel_' + str(a)
        bpy.context.object.name = name
            
        bpy.data.objects[ name ].select = True

        if ( 'color' in lookup[ a ] and pallette is not None ):

          red    = int( pallette[ int( lookup[ a ]['color'] ) ]['red'  ] );
          green  = int( pallette[ int( lookup[ a ]['color'] ) ]['green'] );
          blue   = int( pallette[ int( lookup[ a ]['color'] ) ]['blue' ] );

          matName = tohex( red, green, blue );

          if not matName in bpy.data.materials:

            my_mat = bpy.data.materials.new( matName )
            my_mat.use_nodes = True

            lookupShader = [
             { 'nodeName': 'Material Output', 'shaderName': 'ShaderNodeOutputMaterial', 'location': ( 0.0, 0.0 ) },
             { 'nodeName': 'Mix Shader'     , 'shaderName': 'ShaderNodeMixShader'     , 'location': ( -200.0, 0.0 ) },
             { 'nodeName': 'Glossy BSDF'    , 'shaderName': 'ShaderNodeBsdfGlossy'    , 'location':  (-400.0, -100.0 ) },
             { 'nodeName': 'Diffuse BSDF'   , 'shaderName': 'ShaderNodeBsdfDiffuse'   , 'location': ( -400.0, 100.0 ) },
            ]

            for a in range( 0, len(lookupShader)):
                if not lookupShader[a]['nodeName'] in my_mat.node_tree.nodes:
                    cur_node = my_mat.node_tree.nodes.new( lookupShader[a]['shaderName'] )
                    cur_node.location = lookupShader[a]['location'] 
                else:
                    my_mat.node_tree.nodes[ lookupShader[a]['nodeName'] ].location =  lookupShader[a]['location'] 


            link00 = ['Diffuse BSDF','BSDF','Mix Shader','Shader']
            link01 = ['Glossy BSDF','BSDF','Mix Shader','Shader']
            link02 = ['Mix Shader','Shader','Material Output','Surface']

            links = [link00, link01, link02]
            node_target = 1
            for link in links:
                from_node = my_mat.node_tree.nodes[link[0]]
                output_socket = from_node.outputs[link[1]]
                to_node = my_mat.node_tree.nodes[link[2]]
                if link[0] in ['Glossy BSDF', 'Diffuse BSDF']:
                    input_socket = to_node.inputs[node_target]
                    node_target += 1
                else:
                    input_socket = to_node.inputs[link[3]]
                my_mat.node_tree.links.new(output_socket, input_socket)

            nodes = my_mat.node_tree.nodes

            red   /= 255.0;
            green /= 255.0;
            blue  /= 255.0;

            node = nodes['Diffuse BSDF']
            node.inputs['Color'].default_value = ( red, green, blue, 1.0)
            node.inputs['Roughness'].default_value = 0.0

            node = nodes['Mix Shader']
            node.inputs[0].default_value = 0.05

          bpy.data.objects[ name ].active_material = bpy.data.materials[matName]
     



        bpy.data.objects[ name ].parent = empty

    bpy.context.scene.update()


#//////////////////////////////////////////////////////////////////////////
#
#//////////////////////////////////////////////////////////////////////////

def initScene():
    global voxelSize

    empty = bpy.data.objects.new('container_voxels', None)
    empty.empty_draw_type = 'PLAIN_AXES'
    bpy.context.scene.objects.link(empty)
    bpy.context.scene.update()


    addVoxels( empty )

#//////////////////////////////////////////////////////////////////////////
#
#//////////////////////////////////////////////////////////////////////////

nullifyScene()
initScene()
