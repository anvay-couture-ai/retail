from sqlalchemy import (
    ARRAY,
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
    func,
)
from sqlalchemy.ext.declarative import declarative_base
from clickhouse_sqlalchemy import engines, types

# import types
Base = declarative_base()


class ProductDetails(Base):
    __tablename__ = "distributed_metdata_16122024_latest_schema"

    # __tablename__ = "catalog_15102024"
    # __tablename__ = "catalog_uat_15102024"

    id = Column(String)
    point_id = Column(String, primary_key=True)
    brickheel_en_string_mv = Column(String)
    verticalsizegroup_en_string_mv = Column(String)
    img_288Wx360H_string = Column(String)
    toysverticalactivitytype_en_string_mv = Column(String)
    brickskirtlength_en_string_mv = Column(String)
    _version_ = Column(Integer)
    p_custom_color = Column(ARRAY(String))
    verticalweightrange_string = Column(String)
    spellcheck_en = Column(ARRAY(String))
    l1l3nestedcategory_en_string_mv = Column(ARRAY(String))
    hsnCode_string = Column(String)
    feature_string_mv = Column(ARRAY(String))
    l2category_string_mv = Column(ARRAY(String))
    dod_price_inr_double = Column(Float)
    bricksport_en_string_mv = Column(String)
    relevancyLastModifiedTimestamp_date = Column(DateTime)
    brickclasptype_en_string_mv = Column(String)
    bricktoeshape_en_string_mv = Column(String)
    verticaldialcolor_en_string_mv = Column(String)
    brickFeature_string = Column(String)
    brickSkinTone_string = Column(String)
    brickdistress_en_string_mv = Column(String)
    bricklength_en_string_mv = Column(String)
    brickdupattafabric_en_string_mv = Column(String)
    p_bricksolematerial_text_en_mv = Column(String)
    ageing_double = Column(Float)
    img_280Wx351H_string = Column(String)
    boostingScore_rilfnl_premiumcustexp = Column(Float)
    l1l2category_en_string_mv = Column(ARRAY(String))
    verticalstonetype_en_string_mv = Column(String)
    price_inr_float = Column(Float)
    size_en_string = Column(String)
    segmenthighlight_text_en_mv = Column(String)
    verticalstyletype_en_string_mv = Column(String)
    img_174Wx218H_string = Column(String)
    categoryName_text_en_mv = Column(ARRAY(String))
    verticaldialshape_en_string_mv = Column(String)
    catalogCommercialType_string = Column(String)
    segmenttrendtheme_en_string_mv = Column(String)
    verticalstrapcolor_en_string_mv = Column(String)
    rraattributesLastModifiedTimestamp_date = Column(DateTime)
    boostingScore_jiopoint = Column(Float)
    bricksecondarycolor_en_string_mv = Column(String)
    segmentcharacter_en_string_mv = Column(String)
    earlyAccessPrice_float = Column(Float)
    toysVerticalCharacter_en_string_mv = Column(String)
    brickembroiderytype_en_string_mv = Column(String)
    price_inr_double = Column(Float)
    exactdiscount_int = Column(Integer)
    brickprimarycolor_en_string_mv = Column(String)
    verticalcare_en_string_mv = Column(String)
    tags_string_mv = Column(ARRAY(String))
    averageRating_double = Column(Float)
    exclusiveTill_date = Column(DateTime)
    p_occasion_text_en_mv = Column(String)
    bricklensfeature_en_string_mv = Column(String)
    catalogId = Column(String)
    dod_enabled_int = Column(Integer)
    verticalsizegroupformat_en_string_mv = Column(String)
    genderfilter_en_string_mv = Column(ARRAY(String))
    brickcfscategory_en_string_mv = Column(String)
    golivedays_int = Column(Integer)
    verticalfabriccomposition_string = Column(String)
    brickframeshape_en_string_mv = Column(String)
    boostingScore_rilfnl_couture_model = Column(Float)
    brickMaterialFeature_en_string_mv = Column(String)
    brickblousefabric_en_string_mv = Column(String)
    bricksettype_en_string_mv = Column(String)
    brickSpfQuotient_string = Column(String)
    brickbottomwearfabric_en_string_mv = Column(String)
    bricklapel_en_string_mv = Column(String)
    brickwiring_en_string_mv = Column(String)
    segmentProductTagValidity_date = Column(String)
    # segmentProductTagValidity_string = Column(String)
    boostingScore_rilfnl_non_premium_couture_model = Column(Float)
    p_brickprimarycolor_text_en_mv = Column(String)
    brickaccent_en_string_mv = Column(String)
    bsNumberofPillowCovers_int = Column(Integer)
    boostingScore_rilfnl_premium = Column(Float)
    colorGroup_string = Column(String)
    importedBy_string = Column(String)
    countryOfOrigin_string = Column(String)
    allCategories_string_mv = Column(ARRAY(String))
    brickpiece_en_string_mv = Column(String)
    verticalmetalpurity_string = Column(String)
    wasPrice_double = Column(Float)
    l3CategoryCode_Name_string_mv = Column(ARRAY(String))
    p_bricktoeshape_text_en_mv = Column(String)
    brandName_text_en_mv = Column(String)
    brickanklestyle_en_string_mv = Column(String)
    commercialTypeDiscountRange_string = Column(String)
    brickfittype_en_string_mv = Column(String)
    p_verticalsubcategory_text_en_mv = Column(String)
    verticalClosureType_en_string_mv = Column(String)
    verticalsizeformat_en_string_mv = Column(String)
    p_size_text_en_mv = Column(String)
    verticalcustomisable_string = Column(String)
    pricerange_inr_string = Column(String)
    boostingScore_rilfnl_nonpremium_women_exp = Column(Float)
    catalogVersion = Column(String)
    segmentusp_text_en_mv = Column(String)
    brickstyletype_en_string_mv = Column(String)
    brickcoverage_en_string_mv = Column(String)
    bsType_en_string_mv = Column(String)
    toysverticalskills_en_string_mv = Column(String)
    verticalcolorfamily_en_string_mv = Column(String)
    exclusivetillfilter_string_mv = Column(String)
    brickheelheight_en_string_mv = Column(String)
    cfsClass_text_en = Column(String)
    bricksolematerial_en_string_mv = Column(String)
    verticalbodytype_en_string_mv = Column(String)
    brickfeature1_en_string_mv = Column(String)
    brickSkinType_string = Column(String)
    dod_discount_string = Column(String)
    eanNumber_en_string = Column(String)
    img_473Wx593H_string = Column(String)
    verticaldesigntype_string = Column(String)
    bricktype_en_string_mv = Column(String)
    name_text_en = Column(String)
    verticalwashcare_en_string_mv = Column(String)
    brickpadding_en_string_mv = Column(String)
    verticalcolorshade_en_string_mv = Column(String)
    l3categoryName_string_mv = Column(ARRAY(String))
    isCodDisabled_boolean = Column(Boolean)
    webcategory_string_mv = Column(ARRAY(String))
    dod_pricerange_string = Column(String)
    inStockCount_double = Column(Float)
    brickcapsuleid_en_string_mv = Column(String)
    verticalstrapwidth_en_string_mv = Column(String)
    brickbottomweartype_en_string_mv = Column(String)
    rating_string_mv = Column(ARRAY(String))
    boostingScore_rilfnl_backup = Column(Float)
    brickdresslength_en_string_mv = Column(String)
    brickframefeature_en_string_mv = Column(String)
    verticalstrapmaterial_en_string_mv = Column(String)
    futureListPrice_inr_double = Column(Float)
    inTakeMarginPerc_double = Column(Float)
    bricktraditionalweave_en_string_mv = Column(String)
    fabricdescription_en_string_mv = Column(String)
    inventoryLastModifiedTimestamp_date = Column(DateTime)
    tradeDiscountedValue_double = Column(Float)
    verticalColorHighlight_en_string_mv = Column(String)
    brickcompatibledevices_en_string_mv = Column(String)
    brickwash_en_string_mv = Column(String)
    verticalmaterialtype_en_string_mv = Column(String)
    productToggleOn_string = Column(String)
    allWidgets_string_mv = Column(ARRAY(String))
    brickMaterial_en_string_mv = Column(String)
    brickwaistrise_en_string_mv = Column(String)
    brandtype_en_string_mv = Column(String)
    bricksleeve_en_string_mv = Column(String)
    dod_exactdiscount_int = Column(Integer)
    brickcfsclass_en_string_mv = Column(String)
    numUserRatings_int = Column(Integer)
    brandtype_string_mv = Column(String)
    brickpacktype_en_string_mv = Column(String)
    verticalfabrictype_en_string_mv = Column(String)
    l1l3category_en_string_mv = Column(String, primary_key=True)
    segmentProductTag_string = Column(String)
    verticalsubcategory_en_string_mv = Column(String)
    brickhiddendetail_text_en_mv = Column(String)
    inventoryNodes_string_mv = Column(ARRAY(String))
    brickbuttonclosure_en_string_mv = Column(String)
    verticaldialheight_en_string_mv = Column(String)
    inStockFlag_boolean = Column(Boolean)
    brickCompatibleDevice_en_string_mv = Column(String)
    brickcatgtype_string_mv = Column(ARRAY(String))
    seasonCodeYear_string = Column(String)
    brickcare_en_string_mv = Column(String)
    bricksizeformat_en_string_mv = Column(String)
    discountType_string = Column(String)
    segmentmood_text_en_mv = Column(String)
    brickdesign_en_string_mv = Column(String)
    catalogId_en_string = Column(String)
    category_string_mv = Column(ARRAY(String))
    p_verticalcolorfamily_text_en_mv = Column(String)
    brickCharacter_en_string_mv = Column(String)
    catalogLastModifiedTimestamp_date = Column(DateTime)
    boostingScore_rilfnl_ratings_non_premium = Column(Float)
    creationtime_date = Column(DateTime)
    mrp_double = Column(Float)
    boostingScore_rilfnl_default_copy = Column(Float)
    verticalfeature2_en_string_mv = Column(String)
    brickfeature2_en_string_mv = Column(String)
    l3category_string_mv = Column(ARRAY(String))
    bricktechnique_en_string_mv = Column(String)
    brickTheme_en_string_mv = Column(String)
    priceValue_inr_double = Column(Float)
    toysverticalbatteryrequirement_en_string_mv = Column(String)
    discount_string = Column(String)
    brickuppermaterial_en_string_mv = Column(String)
    occasion_en_string_mv = Column(String)
    brickbacktype_en_string_mv = Column(String)
    brickfitting_en_string_mv = Column(String)
    img_thumbNail_string = Column(String)
    p_brickstyletype_text_en_mv = Column(String)
    bricksize_en_string_mv = Column(String)
    p_brickpattern_text_en_mv = Column(String)
    commercialType_string = Column(String)
    code_string = Column(String)
    bricklaptopsize_en_string_mv = Column(String)
    dod_price_inr_float = Column(Float)
    brickpattern_en_string_mv = Column(String)
    extraImages_string_mv = Column(ARRAY(String))
    boostingScore_rilfnl_premium_product_ranking = Column(Float)
    img_1117Wx1400H_string = Column(String)
    planningCategory_text_en = Column(String)
    img_286Wx359H_string = Column(String)
    l1category_string_mv = Column(ARRAY(String))
    p_brickuppermaterial_text_en_mv = Column(ARRAY(String))
    brickfeaturedetail_text_en_mv = Column(String)
    p_bricksizeformat_text_en_mv = Column(String)
    verticalfeature1_en_string_mv = Column(String)
    brickfrontstyle_en_string_mv = Column(String)
    brickcollar_en_string_mv = Column(String)
    boostingScore_rilfnl_nonpremium = Column(Float)
    bricksizedetail_en_string_mv = Column(String)
    boostingScore_rilfnl_ratings_premium = Column(Float)
    marketedBy_string = Column(String)
    verticaldialwidth_en_string_mv = Column(String)
    inStockPerc_double = Column(Float)
    verticalmetaltype_string = Column(String)
    goliveage_string = Column(String)
    brickneckline_en_string_mv = Column(String)
    boostingScore_rilfnl = Column(Float)
    priceLastModifiedTimestamp_date = Column(DateTime)
    toysverticalagegroup_en_string_mv = Column(String)
    brickConditions_string = Column(String)
    brand_string_mv = Column(String)
    bsThreadCount_string = Column(String)
    verticaljewellerytype_string = Column(String)
    outfitPicture_string = Column(String)
    url_en_string = Column(String)
    global_product_score = Column(Float)


class BaseProductDetailsJiomart(Base):
    """
    Contails the lastest product details schema (catalog schema)
    """

    __abstract__ = True

    point_id = Column(String)
    sku_id_internal = Column(Integer)
    sku_id = Column(String, primary_key=True)
    product_option_id = Column(String)
    product_name = Column(String)
    product_description = Column(String)
    medias = Column(types.Map(String, String))
    url_slug = Column(String)

    # Relevancy
    popularity_score = Column(Float)

    # price
    # discount = Column(Float)
    price_range = Column(String)
    # price = Column(Float)
    avg_mrp = Column(Float)

    # Tags
    promotions = Column(ARRAY(String))
    # tags = Column(ARRAY(String))
    payment_tag_todate = Column(String)
    payment_tag = Column(String)
    tag_todate = Column(String)
    tag = Column(String)

    # cateogry names (present in the catalog table)
    # l0 = Column(ARRAY(String))
    # l1 = Column(ARRAY(String))
    # l2 = Column(ARRAY(String))
    # l3 = Column(ARRAY(String))
    # l4 = Column(ARRAY(String))

    # cateogry names and IDs (present in the data ingestion table - requires mapping)
    category_name_level0 = Column(ARRAY(String))
    category_name_level1 = Column(ARRAY(String))
    category_name_level2 = Column(ARRAY(String))
    category_name_level3 = Column(ARRAY(String))
    category_name_level4 = Column(ARRAY(String))

    category_id_level0 = Column(ARRAY(Integer))
    category_id_level1 = Column(ARRAY(Integer))
    category_id_level2 = Column(ARRAY(Integer))
    category_id_level3 = Column(ARRAY(Integer))
    category_id_level4 = Column(ARRAY(Integer))

    # l1l2l4_category = Column(ARRAY(String))
    # l1l2l3_category = Column(ARRAY(String))
    # brand_name = Column(String)
    color = Column(String)
    # attributes = Column(String)

    # inventory - store related
    mart_availability = Column(String)
    vertical_code = Column(String)
    inventory_stores = Column(ARRAY(String))
    inventory_stores_3p = Column(ARRAY(String))

    # variants
    variants = Column(String)

    # inventory - stock related
    in_stock = Column(Boolean)

    # manufacturer details
    manufacturer_name = Column(String)
    manufacturer_id = Column(Integer)

    # extras
    average_rating = Column(Float)
    avg_selling_price = Column(Float)
    avg_discount_pct = Column(Float)
    avg_discount_rate = Column(Float)
    avg_discount = Column(Float)
    number_of_user_ratings = Column(Integer)
    # payment_tags = Column(ARRAY(String))
    # is_available = Column(Integer)
    product_theme = Column(String)
    # applicable_stores = Column(ARRAY(String))
    applicable_regions = Column(ARRAY(String))
    brand_id = Column(Integer)
    product_attributes = Column(String)
    brand = Column(String)


class ProductDetailsJiomart(BaseProductDetailsJiomart):
    __tablename__ = "catalog_jiomart_ingestion"
