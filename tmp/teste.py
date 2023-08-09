import ezdxf

def rotate_entity(entity, angle_degrees, rotation_center):
    # Calcula o ângulo em radianos
    angle_radians = angle_degrees * (3.141592653589793 / 180.0)
    
    # Realiza a rotação da entidade
    entity.rotate_z(angle_radians)

# Caminho para o arquivo DXF de entrada e saída
input_file_path = 'caminho_para_arquivo_entrada.dxf'
output_file_path = 'caminho_para_arquivo_saida.dxf'

# Ângulo de rotação em graus
angle_degrees = 45.0

# Ponto central de rotação (coordenadas X e Y)
rotation_center = (0.0, 0.0)

# Abre o arquivo DXF de entrada
doc = ezdxf.readfile('tmp/teste1.dxf')

# Seleciona a entidade que você deseja rotacionar (por exemplo, uma linha)
entity = doc.modelspace().query('LINE')[0]

# Rotaciona a entidade
rotate_entity(entity, angle_degrees, rotation_center)

# Salva as alterações no arquivo de saída
doc.saveas(output_file_path)

print("Entidade rotacionada e salva em", output_file_path)
