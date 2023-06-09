class LoginResult {
    login_token: str
    fail_message: str
}

class ParseResult {
	is_success: bool
	fail_reason: str
}

class 联系方式 {
	固话: str
	手机: str
}
class 从业人员数量信息 {
	平均人数: int
	在岗人数: int
	劳务派遣人数: int
}
class FixDecimal {
	integer: int
	decimal: int
}
class 从业人员工资总额 {
	从业人员工资总额: FixDecimal
	在岗职工工资总额: FixDecimal
	劳务派遣人员工资总额: FixDecimal
}
class 企业主要经济指标及企业人工成本指标 {
	"销售（营业）收入": FixDecimal
	利润总额: FixDecimal
	固定资产折旧: FixDecimal
	主营业务税金及附加: FixDecimal
	成本费用总额: FixDecimal
	人工成本总计: FixDecimal
	从业人员工资总额: 从业人员工资总额
	福利费用: FixDecimal
	教育经费: FixDecimal
	保险费用: FixDecimal
	劳动保护费用: FixDecimal
	住房费用: FixDecimal
	其他人工成本: FixDecimal
}

class CompanyBrief {
	统一社会信用代码: str
	组织机构代码: str
	法人单位名称: str
	"法定代表人 （单位负责人）": str
	联系方式: 联系方式
	企业所在地行政区划代码: 地域s
	单位隶属关系: 单位隶属关系s
	行业类别代码: 行业类别代码s
	企业规模: 企业规模s
	登记注册类型: 登记注册类型s
	从业人员数量信息: 从业人员数量信息
}

class CompanyListInfo {
	current_page: int
	max_page: int
	data: List[CompanyBrief]
}

class 从业人员工资报酬信息{
	职工代码: int
	性别: 性别s
	出生年份: int
	学历: 学历s
	参加工作年份: int
	职业: 职业s
	"管理岗位/专业技术职称/职业技能等级": str
	用工形式: 用工形式s
	劳动合同类型: 劳动合同类型s
	全年周平均工作小时数: int
	是否工会会员: bool
	全年工资报酬合计: FixDecimal
	"基本工资（类）": FixDecimal
	"绩效工资（类)": FixDecimal
	"津补贴（类）": FixDecimal
	加班加点工资: FixDecimal
}

class CompanyInfo: CompanyBrief {
	企业主要经济指标及企业人工成本指标: 企业主要经济指标及企业人工成本指标
	从业人员工资报酬信息: List[从业人员工资报酬信息]
	had_commited: bool
}

class CommitRecord{
	_id: ObjectId
	company_id: ObjectId
	file_path: str
}