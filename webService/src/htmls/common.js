const PATH_UPLOAD = 'http://127.0.0.1:9090/uploadImg'

$(document).ready(function(){
       
    // 正面checkbox
    $(".img_state_front").change(function(){
        update_kind($(this), '.img_state_front')
    });

    // 侧面checkbox    
    $(".img_state_side").change(function(){
        update_kind($(this), '.img_state_side')
    });

    // 反面checkbox
    $(".img_state_obverse").change(function(){
        update_kind($(this), '.img_state_obverse')
    });

    // 提交按钮
    $('.btn_submit').click(function(){
        upload_good_info($(this))
    });
    
    /**
     * 更新图片选中的类型
     * @param {*} img_obj 
     * @param {*} img_state 
     */
    function update_kind(img_obj, img_state){

        // 1.查看其他图片同状态的checkbox是否选中,并更新
        update_same_kind(img_obj, img_state)

        // 2.查看相同图片的其他checkbox是否选中, 并更新
        update_other_kind(img_obj, img_state)
    }

    /**
     * 更新该商品其他图片相同类型的CheckBox的状态
     * @param {*} img_obj 
     * @param {*} img_state 
     */
    function update_same_kind(img_obj, img_state){

        var td = img_obj.parent().parent().parent()

        var check_list = td.find(img_state)

        if(img_obj.prop('checked')){                    // 如果选中, 1.遍历其他的checkbox 将他们的置为未选中;2.更新商品的图片信息
            
            check_list.each(function(){
                if($(this).prop('checked'))
                    $(this).prop('checked', false)
            })

            img_obj.prop('checked', true)
            
        }else{                                          // 如果没有选中,

        }
    }


    /**
     * 更新该商品同一图片不同类型的CheckBox的状态
     * @param {*} img_obj 
     * @param {*} img_state 
     */
    function update_other_kind(img_obj, img_state){
        var ck_list = img_obj.parent().find('input[type="checkbox"]')

        if(img_obj.prop('checked')){                    // 如果选中, 1.遍历其他的checkbox 将他们的置为未选中;2.更新商品的图片信息
            
            ck_list.each(function(){
                if($(this).prop('checked'))
                        $(this).prop('checked', false)
            })
            img_obj.prop('checked', true)
            
        }else{                                          // 如果没有选中,

        }

        
    }

    /**
     * 上传 商品信息
     * @param {} btn_sub 
     */
    function upload_good_info(btn_sub){

        // 获取商品信息
        var p_list = btn_sub.parent().find('p')
        if(p_list.length != 11) return

        var good_info = {
            good_name:      $(p_list[0]).text(),        // 商品名称
            good_upc:       $(p_list[1]).text(),        // 商品编码
            good_first:     $(p_list[2]).text(),        // 商品一级分类
            good_second:    $(p_list[3]).text(),        // 商品二级分类
            good_third:     $(p_list[4]).text(),        // 商品三级分类
            good_desc:      $(p_list[5]).text(),        // 商品描述
            good_price:     $(p_list[6]).text(),        // 商品价格
            good_id:        $(p_list[7]).text(),        // 商品id
            good_p:         $(p_list[8]).text(),        // 商品省
            good_c:         $(p_list[9]).text(),        // 商品市
            good_x:         $(p_list[10]).text(),       // 商品区县
        }

        // 获取选择的图片信息
        img_front_list = btn_sub.parent().next().find('.img_state_front')
        img_side_list = btn_sub.parent().next().find('.img_state_side')
        img_obverse_list = btn_sub.parent().next().find('.img_state_obverse')

        img_front_list.each(function(){
            if($(this).prop('checked')){
                good_info['img_front'] = $(this).parent().next().attr('href')
            }
        })

        img_side_list.each(function(){
            if($(this).prop('checked')){
                good_info['img_side'] = $(this).parent().next().attr('href')
            }
        })

        img_obverse_list.each(function(){
            if($(this).prop('checked')){
                good_info['img_obverse'] = $(this).parent().next().attr('href')
            }
        })

        if(good_info['img_front'] || good_info['img_side'] || good_info['img_obverse']){
            
            // 禁用按钮
            btn_sub.text('正在提交...')
            btn_sub.prop('disabled', 'disabled') 

            // 提交数据
            $.post(PATH_UPLOAD, good_info, function(result){
                data =JSON.parse(result)
                if('0000' == data.returnCode){
                    btn_sub.text('提交完成')
                }else{
                    btn_sub.text('提交失败,重新提交')
                    btn_sub.prop('disabled', '') 
                }
                
            })

        }
    }

});

/**
 * 加载资源
 * @param {*} path  资源路径
 * @param {*} title 资源标题
 */ 
function load_source(path, title){
    document.getElementById('source').setAttribute('src', path)
    document.getElementById('title').innerText = title
}
