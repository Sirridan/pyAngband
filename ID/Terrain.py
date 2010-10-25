#ID.Terrain
#TF = Terrain Feature
import ID.Ranges

( TF_NONE,
  TF_DARKNESS,
  TF_FLOOR,
  TF_PERMA,
  TF_GRANITE,
  TF_QUARTZ,
  TF_MAGMA,
  TF_GRANITE_VEIN,
  TF_QUARTZ_VEIN,
  TF_MAGMA_VEIN,
  TF_DOOR_CLOSED,
  TF_DOOR_LOCKED,
  TF_DOOR_BROKEN,
  TF_DOOR_OPEN,
  TF_SHOP_GENERAL,
  TF_SHOP_ARMORY,
  TF_SHOP_SMITH,
  TF_SHOP_TEMPLE,
  TF_SHOP_ALCHEMY,
  TF_SHOP_MAGIC,
  TF_SHOP_BLACKMARKET,
  TF_SHOP_HOME) = range(ID.Ranges.TERRAIN_START, ID.Ranges.TERRAIN_END)