import matplotlib.pyplot as plt
import matplotlib.patches as patch

def draw_court(ax=None, key_color = 'orange'):
    plt.figure(figsize=(4.7/2,5/2))
    if ax is None:
        ax = plt.gca()
    
    # Court Background
    court_bg = patch.Rectangle((0,0), 47*12, 50*12, color = "#DEB886")
    
    # Court Outline
    court_outline_left = patch.Rectangle((-8,-8), 8, 616, color = 'black')
    court_outline_top = patch.Rectangle((-8,600), 572, 8, color = 'black')
    court_outline_bottom = patch.Rectangle((-8,-8), 572, 8, color = 'black')
    mid_line = patch.Rectangle((563, 0), 1, 600, color = 'black')
    
    # Hoop
    rim = patch.Circle((63, 300), radius=9, linewidth = 1, color='black', fill=False)
    backboard = patch.Rectangle((46, 264), 1, 72, color='black', fill=True)
    back_iron = patch.Rectangle((48, 295.5), 6, 9, color='black', fill=True)
    
    # 3 Point Lines
    three_pt_bottom = patch.Rectangle((0, 40.125), 118.375, 2, color='black')
    three_pt_top = patch.Rectangle((0, 557.875), 118.375, 2, color='black')
        
    # Key
    key_bottom = patch.Rectangle((0,228), 228, 2, color='black')
    key_top = patch.Rectangle((0,370), 228, 2, color='black')
    free_throw_line = patch.Rectangle((226, 228), 2, 144, color='black')
    
    # Block/hashes
    block_bottom = patch.Rectangle((84, 218), 12, 8, color='black', fill=True)
    block_top = patch.Rectangle((84, 372), 12, 8, color='black', fill=True)
    hash1_bottom = patch.Rectangle((132, 218), 2, 8, color='black', fill=True)
    hash2_bottom = patch.Rectangle((170, 218), 2, 8, color='black', fill=True)
    hash3_bottom = patch.Rectangle((208, 218), 2, 8, color='black', fill=True)
    hash1_top = patch.Rectangle((132, 372), 2, 8, color='black', fill=True)
    hash2_top = patch.Rectangle((170, 372), 2, 8, color='black', fill=True)
    hash3_top = patch.Rectangle((208, 372), 2, 8, color='black', fill=True)
    baseline_hash_bottom = patch.Rectangle((0, 190), 12, 2, color='black')
    baseline_hash_top = patch.Rectangle((0, 408), 12, 2, color='black')
    
    # Restricted Zone Lines
    rz_bottom = patch.Rectangle((48, 252), 15, 2, color='black', fill=True)
    rz_top = patch.Rectangle((48, 346), 15, 2, color='black', fill=True)
    
    # Arcs
    three_pt_arc = patch.Arc((63, 300), 265*2, 265*2, theta1 = 282, theta2 = 438, linewidth = 1.6)    
    free_throw_arc = patch.Arc((228, 300), 142, 142, theta1 = 270, theta2 = 90, linewidth = 1.6)
    center_arc = patch.Arc((564, 300), 144, 144, theta1 = 90, theta2 = 270, linewidth = 1.6)
    restricted_arc = patch.Arc((63, 300), 94, 94, theta1 = 270, theta2 = 90, linewidth = 1.6)
    
    
    court_elements = [court_bg, 
                      court_outline_left, 
                      court_outline_top, 
                      court_outline_bottom,
                      mid_line,
                      rim,
                      backboard,
                      back_iron,
                      three_pt_bottom,
                      three_pt_top,
                      key_bottom,
                      key_top,
                      free_throw_line,
                      block_bottom,
                      block_top,
                      hash1_bottom,
                      hash2_bottom,
                      hash3_bottom,
                      hash1_top,
                      hash2_top,
                      hash3_top,
                      baseline_hash_bottom,
                      baseline_hash_top,
                      three_pt_arc,
                      free_throw_arc,
                      center_arc,
                      restricted_arc,
                      rz_bottom,
                      rz_top]
    
    for element in court_elements:
        ax.add_patch(element)
    
    # major_ticks = np.arange(-3, 101, 1)
    # ax.set_xticks(major_ticks)
    # ax.set_yticks(major_ticks)    
    # ax.grid()
    ax.axis("off")
    plt.xlim(-20,580)
    plt.ylim(-20,620)
    plt.gcf().set_dpi(300)
    # plt.show()
    
    return ax