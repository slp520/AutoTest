list = {'code': 200, 'data': {'perMissionTreeOutputs': [
    {'content': 'root', 'id': 100113, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'root', 'subPermissionTrees': [
        {'content': '首页', 'id': 100114, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'main_tab',
         'subPermissionTrees': [
             {'content': '录订单', 'id': 100115, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'record_order'},
             {'content': '确认带看', 'id': 100116, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'confirm_guide'},
             {'content': '接拒收', 'id': 100117, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'accept_reject'}]},
        {'content': '客户', 'id': 100118, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'customer_tab',
         'subPermissionTrees': [{'content': '确认业绩', 'id': 100121, 'order': 0, 'perMissionFlag': 0,
                                 'permissionName': 'confirm_performance'}]},
        {'content': '订单', 'id': 100126, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'order_tab',
         'subPermissionTrees': [
             {'content': '录订单1', 'id': 100127, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'record_order1'}]},
        {'content': '流程', 'id': 100122, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'process_tab',
         'subPermissionTrees': [
             {'content': '异常申诉', 'id': 100123, 'order': 0, 'perMissionFlag': 0, 'permissionName': 'exception_complain'},
             {'content': '优惠券兑换', 'id': 100124, 'order': 0, 'perMissionFlag': 0,
              'permissionName': 'exchange_coupon'}]}]}],
    'token': '68eddc22572e4efb',
                              'user': {'avatar': 'https://fsupload.fangdd.com/image/JQE068w8hO6IFYxtzofoXrlbguI.jpg',
                                       'cityName': '上海', 'companyName': '测试自营分公司', 'disabled': 0, 'maxRoleName': '项目经理',
                                       'minRoleName': '项目经理', 'mobile': '15507592070', 'nickName': '新体验项目助理',
                                       'ocUserId': 408899, 'realName': '新体验', 'userId': 408899, 'userName': '新体验项目助理'}},
        'success': True}

t = list['data']
print(t['token'])
