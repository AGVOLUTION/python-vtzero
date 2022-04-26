from vtzero.tile import VectorTile, Tile, Layer, Point, Polygon, Linestring

# https://github.com/tilery/python-vtzero

tile = Tile()
points = Layer(tile, b'points')
feature = Point(points)
feature.set_id(1)
feature.add_points(1)
feature.set_point(10, 10)
# feature.add_property_string(b'foo', b'bar')
# feature.add_property_string(b'x', b'178.64039611816406')
# feature.add_property_string(b'y', b'206.67601013183594')
# feature.add_property_float(b'x', 178.64039611816406)
# feature.add_property_float(b'y', 206.67601013183594)
feature.add_property_uint64_t(b'x', 5)
feature.add_property_uint64_t(b'y', 6)
# feature.add_property_uint64_t(b'x', round(178.64039611816406))
# feature.add_property_uint64_t(b'y', (2**64)-1)
feature.commit()

# Encode mvt
data = tile.serialize()
print("size:", len(data))

with open('test.pbf', 'wb') as f:
    f.write(data)

# Decode MVT and print info
tile = VectorTile(data)
layer = next(tile)

print(f"Layer Name: {layer.name.decode()}")
print(f"MVT version: {layer.version}")
print(f"MVT extent: {layer.extent}")
features = []
while True:
    f = next(layer)
    if f.geometry_type == 0:
        break
    features.append(f)
print(f"Nb Features: {len(features)}")

for feat in features:
    print(feat.id)