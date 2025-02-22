from tables.models import WellData, VLP


def get_check_well_data_exists(session, well_data_hash):
    """
    Checks if the well_data table exists.
    
    :param session:
    :param well_data:
    :return:
    """
    well_id = session.query(WellData.id).filter(
        WellData.id == well_data_hash).scalar()

    return well_id


def save_well_data(session, init_data):
    well_data = WellData(

    MD=init_data.inclinometry.MD,
    TVD = init_data.inclinometry.TVD,
    d_casing = init_data.casing.d,
    d_tubing = init_data.tubing.d,
    h_mes_tubing = init_data.tubing.h_mes,
    wct = init_data.pvt.wct,
    rp = init_data.pvt.rp,
    gamma_oil = init_data.pvt.gamma_oil,
    gamma_gas = init_data.pvt.gamma_gas,
    gamma_wat = init_data.pvt.gamma_wat,
    t_res = init_data.pvt.t_res,
    p_wh = init_data.p_wh,
    geo_grad = init_data.geo_grad,
    h_res = init_data.h_res
    )

    session.add(well_data)
    session.commit()


# id=well_data_id,
# inclinometry=init_data["inclinometry"],
# d_cas=init_data["casing"]["d"],
# d_tub=init_data["tubing"]["d"],
# h_tub=init_data["tubing"]["h_mes"],
# wct=init_data["pvt"]["wct"],
# rp=init_data["pvt"]["rp"],
# gamma_oil=init_data["pvt"]["gamma_oil"],
# gamma_gas=init_data["pvt"]["gamma_gas"],
# gamma_wat=init_data["pvt"]["gamma_wat"],
# t_res=init_data["pvt"]["t_res"],
# p_wh=init_data["p_wh"],
# geo_grad=init_data["geo_grad"],
# h_res=init_data["h_res"]



def get_check_vlp_exists(session, well_id):
    """
    Check if the well_id exists in the session
    :param well_id:
    :return:
    """
    vlp = session.query(VLP.vlp).filter(VLP.well_id == well_id).scalar()
    return vlp
def save_vlp_data(session, init_data):
    q_liq = str(init_data["q_liq"])
    p_wf = str(init_data["p_wf"])
    vlp = VLP(q_liq=q_liq,
              p_wf=p_wf)
    session.add(vlp)
    session.commit()
