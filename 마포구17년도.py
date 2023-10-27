import pandas as pd
import folium
import json

"""
노원구 행정동의 경계에 대한 좌표를 반환한다.    
"""
def extract_nowon_dong() : 

    # 노원구의 행정동 코드를 가지고 있다.
    dong_data = pd.read_csv('./data/mapo_dong_code.csv', encoding='cp949')
    #print(dong_data)

    dong_codes = dong_data['Code']
    #print(dong_codes)

    #geo_simple = pd.read_json('kostat_2013_json_skorea_submunicipalities_geo_simple.json')

    geo_path = './data/kostat.json'
    geo_path_hi = 'skorea-submunicipalities-2018-geo.json'

    geo_data = json.load(open(geo_path, encoding='utf-8'))
    
    #print(geo_simple)

    #nowon_dongs = []
    nowon_dongs = dict()
    nowon_dongs["type"] = "FeatureCollection"
    nowon_dongs["features"] = []
    
    for row in geo_data["features"] :
        #print(row)
        
        dong_code = row['properties']['code']
        #print(type(dong_code))
        
        # 노원구의 행정동인지 검사 (타입이 다름에 주의한다.)
        if dong_codes.astype('str').str.contains(dong_code).any() :
            nowon_dongs["features"].append(row)            
    
    return nowon_dongs

"""
지도에 행정동의 경계를 표시한다.
"""
def map_nowon(geo_data, dong_data) :
    center_of_nowon = [37.56070556, 126.9105306]
    
    gmap = folium.Map(location=center_of_nowon, zoom_start=12.5, tiles='cartodbpositron')
     
    # geo_data as GeoJson   
    fmap = folium.Choropleth(geo_data=geo_data,
                   data=dong_data,
                   columns=['Code', 'Scaled'],
                   fill_color='YlGnBu',
                   key_on='feature.properties.code',
                   highlight=True,
                   fill_opacity=0.7,
                   line_opacity=1,
                   legned_name='Population',

                   ).add_to(gmap)

    # 이렇게 추가해도 되지만, 추가 작업이 필요하다.
    # folium.GeoJson(
    #     geo_data,
    #     name='지역구'
    # ).add_to(gmap)

    folium.LayerControl().add_to(gmap)
    
    #fmap.geojson.zoom_on_click = False
    
    fmap.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], labels=False)
    )
    
    gmap.save('./map_mapo17.html')
    
    gmap.show_in_browser()


def main():
    """ Main entry point of the app """
    
    geo_nowon_dongs = extract_nowon_dong()
    
    #print(geo_nowon_dongs)
        
    # 동별 표시할 정보를 로딩한다. (가상 인구수)
    dong_data = pd.read_csv('./data/mp17_map.csv', encoding='cp949' )
    sc1=dong_data['Counts']
    sc2=(sc1-sc1.min())/(sc1.max()-sc1.min())*100
    dong_data=pd.concat((dong_data, sc2),1)
    dong_data.columns.values[3] = 'Scaled'
    print(dong_data)
    map_nowon(geo_nowon_dongs, dong_data)
    
    # print('Have a good day !')
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()