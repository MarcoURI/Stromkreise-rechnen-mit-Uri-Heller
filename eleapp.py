import pygame 
import sys
import button
import os
import scores
import webbrowser
# start pygame
pygame.init()
screen = pygame.display.set_mode((1920,1060))
try:
    # Portable Pfad-Konfiguration
    def get_image_folders():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Mögliche Basis-Pfade (in Prioritätsreihenfolge)
        possible_bases = [
            script_dir,  # Gleicher Ordner wie das Skript
            os.path.join(script_dir, "Stromkreise rechnen mit Uri Heller"),  # Falls in Unterordner
        ]
        for base_path in possible_bases:
            folders = {
                "ui": os.path.join(base_path, "ggra", "ui"),
                "bbutt": os.path.join(base_path, "ggra", "bbutt"),
                "wider": os.path.join(base_path, "ggra", "wider"),
                "strom": os.path.join(base_path, "ggra", "strom"),
                "span": os.path.join(base_path, "ggra", "span"),
                "sound": os.path.join(base_path, "ggra", "sound"),
            }
            if all(os.path.exists(path) for path in folders.values()):
                return folders
        
        raise FileNotFoundError("Image-Ordner konnten nicht gefunden werden.")
    
    # Ordner ermitteln
    folders = get_image_folders()
    IMAGE_FOLDER1 = folders["ui"]
    IMAGE_FOLDER2 = folders["bbutt"]
    IMAGE_FOLDER3 = folders["wider"]
    IMAGE_FOLDER4 = folders["strom"]
    IMAGE_FOLDER5 = folders["span"]
    IMAGE_FOLDER6 = folders ["sound"]
except pygame.error as e:
    print(f"Pygame Fehler: {e}")
    sys.exit()
except FileNotFoundError as e:
    print(f"Ordner-Fehler: {e}")
    print("Stellen Sie sicher, dass die 'ggra'-Ordner im gleichen Verzeichnis wie das Skript liegen.")
    sys.exit()
# window title 
pygame.display.set_caption("Stromkreise rechnen mit Uri Heller")
# image load
try:
# hauptmenu    
    try:
        # bg
        bg_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'bg.png')).convert_alpha()
        neubg_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'neubg.png')).convert_alpha()
        formbg_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'formbg.png')).convert_alpha() 
        gefabg_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'gefabg.png')).convert_alpha() 
        gesbg_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'gesbg.png')).convert_alpha()  
        playbg_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'playbg.png')).convert_alpha() 
        # uri 
        uristart_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'uristart.png')).convert_alpha()
        urigebiet_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urigebiet.png')).convert_alpha()
        urigrad_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urigrad.png')).convert_alpha()
        uriwiss_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'uriwiss.png')).convert_alpha()
        urihelp_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urihelp.png')).convert_alpha()
        uriber_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'uriber.png')).convert_alpha()
        urigr_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urigr.png')).convert_alpha()
        urigut_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urigut.png')).convert_alpha()
        uriweit_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'uriweit.png')).convert_alpha()
        urimw_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urimw.png')).convert_alpha()
        urina_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urina.png')).convert_alpha()
        uripr_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'uripr.png')).convert_alpha()
        urisp_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urisp.png')).convert_alpha()
        urisuper_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'urisuper.png')).convert_alpha()
        urifort_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'fortschritt.png')).convert_alpha()
        urirech_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'rechner.png')).convert_alpha()
        # menu buttons
        start_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'start.png')).convert_alpha()
        ges_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'ges.png')).convert_alpha()
        form_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'form.png')).convert_alpha()
        gefa_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'gefa.png')).convert_alpha()
        tech_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'tech.png')).convert_alpha()
        # menu learn practice play
        lern_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'lernen.png')).convert_alpha()
        spi_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'spielen.png')).convert_alpha()
        # learn practice play
        phet_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'phet.png')).convert_alpha()
        box_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'box.png')).convert_alpha() 
        mal_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'mal.png')).convert_alpha()
        leifi_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'leifi.png')).convert_alpha()
        muse_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'muse.png')).convert_alpha()
        srf_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'srf.png')).convert_alpha()
        wiki_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'wiki.png')).convert_alpha()
        meg_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'meg.png')).convert_alpha()
        stud_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'stud.png')).convert_alpha()
        suva_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'suva.png')).convert_alpha()
        srf_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'srf.png')).convert_alpha()
        serlo_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'serlo.png')).convert_alpha()
        # menu span wider strom gemisch
        span_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'spannung.png')).convert_alpha()
        wider_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'wider.png')).convert_alpha()
        strom_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'strom.png')).convert_alpha()
        # menu leicht mit schwer
        erklärung_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'erklärung.png')).convert_alpha()
        lei_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'leicht.png')).convert_alpha()
        mit_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'mittel.png')).convert_alpha()
        schwe_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'schwe.png')).convert_alpha()
        # interface
        weit_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'weiter.png')).convert_alpha()
        zurü_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'zurü.png')).convert_alpha()
        exit_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'exit.png')).convert_alpha()
        hmenu_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'hmenu.png')).convert_alpha()
        menuw_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'menu.png')).convert_alpha()
        menustr_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'menu.png')).convert_alpha()
        menusp_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'menu.png')).convert_alpha()
        richtig_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'richtig.png')).convert_alpha()
        falsch_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'falsch.png')).convert_alpha()
        # Erklgrid
        erkl1_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'erkl1.png')).convert_alpha()
        erkl2_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'erkl2.png')).convert_alpha()
        erkl3_img = pygame.image.load(os.path.join(IMAGE_FOLDER1,'erkl3.png')).convert_alpha()
    except pygame.error as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        sys.exit()
# üeben
    # widerstand
    try:
        # leicht    
        erklwser_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'erklwser.png')).convert_alpha()
        erklwpara_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'erklwpara.png')).convert_alpha()
        erklwgruppe_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'erklwgruppe.png')).convert_alpha() 
        WE1_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE1.png')).convert_alpha()
        WE2_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE2.png')).convert_alpha()
        WE3_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE3.png')).convert_alpha()
        WE4_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE4.png')).convert_alpha()
        WE5_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE5.png')).convert_alpha()
        WE6_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE6.png')).convert_alpha()
        WE7_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE7.png')).convert_alpha()
        WE8_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE8.png')).convert_alpha()
        WE9_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE9.png')).convert_alpha()
        WE10_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WE10.png')).convert_alpha()
        # wider leicht richtig
        zwei_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'2ohm.png')).convert_alpha()
        vier_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'4.png')).convert_alpha()
        sex_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'6.png')).convert_alpha()
        acht_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'8.png')).convert_alpha()
        zeh_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'10.png')).convert_alpha()
        zwö_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'12.png')).convert_alpha()
        vierz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'14.png')).convert_alpha()
        sexz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'16.png')).convert_alpha()
        achtz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'18.png')).convert_alpha()
        zwan_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'20.png')).convert_alpha()
        # mit
        erklwskip_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'erklwskip.png')).convert_alpha()
        WM1_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM1.png')).convert_alpha()
        WM2_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM2.png')).convert_alpha()
        WM3_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM3.png')).convert_alpha()
        WM4_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM4.png')).convert_alpha()
        WM5_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM5.png')).convert_alpha()
        WM6_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM6.png')).convert_alpha()
        WM7_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM7.png')).convert_alpha()
        WM8_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM8.png')).convert_alpha()
        WM9_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM9.png')).convert_alpha()
        WM10_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WM10.png')).convert_alpha()
        # wider mit richtig
        hun_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'100.png')).convert_alpha()
        hunz_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'110.png')).convert_alpha()
        hunzwa_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'120.png')).convert_alpha()
        hundre_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'130.png')).convert_alpha()
        hunvie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'140.png')).convert_alpha()
        hunfün_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'150.png')).convert_alpha()
        hunsex_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'160.png')).convert_alpha()
        hunsib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'170.png')).convert_alpha()
        hunacht_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'180.png')).convert_alpha()
        hunneu_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'190.png')).convert_alpha()
        zweihun_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'200.png')).convert_alpha()
        # schwer
        erklwschwer_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'erklwschwer.png')).convert_alpha()
        WS1_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS1.png')).convert_alpha()
        WS2_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS2.png')).convert_alpha()
        WS3_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS3.png')).convert_alpha()
        WS4_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS4.png')).convert_alpha()
        WS5_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS5.png')).convert_alpha()
        WS6_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS6.png')).convert_alpha()
        WS7_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS7.png')).convert_alpha()
        WS8_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS8.png')).convert_alpha()
        WS9_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS9.png')).convert_alpha()
        WS10_img = pygame.image.load(os.path.join(IMAGE_FOLDER3,'WS10.png')).convert_alpha()
        # wider schwer richtig
        sibsib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'77.png')).convert_alpha()
        neusib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'97.png')).convert_alpha()
        hunzwadrei_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'123.png')).convert_alpha()
        hunzwavie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'124.png')).convert_alpha()
        hunzwafü_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'125.png')).convert_alpha()
        hundreivie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'134.png')).convert_alpha()
        hunvievie_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'144.png')).convert_alpha()
        hunfüneu_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'159.png')).convert_alpha()
        hunsibsib_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'177.png')).convert_alpha()
        zweihunein_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'201.png')).convert_alpha()
        # wider falsch
        l220_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'l220.png')).convert_alpha()
        l100200_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'l100200.png')).convert_alpha()
        lschwer_img = pygame.image.load(os.path.join(IMAGE_FOLDER2,'lschwer.png')).convert_alpha()
    except pygame.error as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        sys.exit()
    # strom
    try:
        # leicht    
        erklstrser_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'erklstrser.png')).convert_alpha()
        erklstrpara_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'erklstrpara.png')).convert_alpha()
        erklstrgruppe_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'erklstrgruppe.png')).convert_alpha()
        erklstrleicht_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'erklstrleicht.png')).convert_alpha()
        STL1_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL1.png')).convert_alpha()
        STL2_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL2.png')).convert_alpha()
        STL3_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL3.png')).convert_alpha()
        STL4_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL4.png')).convert_alpha()
        STL5_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL5.png')).convert_alpha()
        STL6_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL6.png')).convert_alpha()
        STL7_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL7.png')).convert_alpha()
        STL8_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL8.png')).convert_alpha()
        STL9_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL9.png')).convert_alpha()
        STL10_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STL10.png')).convert_alpha()
        # strom leicht richtig
        LA_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LA.png')).convert_alpha()
        LB_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LB.png')).convert_alpha()
        LC_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LC.png')).convert_alpha()
        LD_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LD.png')).convert_alpha()
        LE_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LE.png')).convert_alpha()
        LF_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LF.png')).convert_alpha()
        LG_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LG.png')).convert_alpha()
        LH_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LH.png')).convert_alpha()
        LI_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LI.png')).convert_alpha()
        LJ_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LJ.png')).convert_alpha()
        LK_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LK.png')).convert_alpha()
        LA_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'LA.png')).convert_alpha()
        alle_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'alle.png')).convert_alpha()
        # mit
        erklstr1def_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'erklstr1def.png')).convert_alpha()
        erklstr2def_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'erklstr2def.png')).convert_alpha()
        STM1_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM1.png')).convert_alpha()
        STM2_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM2.png')).convert_alpha()
        STM3_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM3.png')).convert_alpha()
        STM4_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM4.png')).convert_alpha()
        STM5_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM5.png')).convert_alpha()
        STM6_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM6.png')).convert_alpha()
        STM7_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM7.png')).convert_alpha()
        STM8_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM8.png')).convert_alpha()
        STM9_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM9.png')).convert_alpha()
        STM10_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STM10.png')).convert_alpha()
        # strom mit richtig
        # schwer
        erklstr1skip_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'erklstr1skip.png')).convert_alpha()
        STS1_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS1.png')).convert_alpha()
        STS2_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS2.png')).convert_alpha()
        STS3_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS3.png')).convert_alpha()
        STS4_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS4.png')).convert_alpha()
        STS5_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS5.png')).convert_alpha()
        STS6_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS6.png')).convert_alpha()
        STS7_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS7.png')).convert_alpha()
        STS8_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS8.png')).convert_alpha()
        STS9_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS9.png')).convert_alpha()
        STS10_img = pygame.image.load(os.path.join(IMAGE_FOLDER4,'STS10.png')).convert_alpha()
        # strom schwer richtig
        # strom falsch
        stromfalsch_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'stromfalsch.png')).convert_alpha()
    except pygame.error as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        sys.exit()
    # spannung
    try:
        # leicht
        erklspan1_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan1.png')).convert_alpha()
        erklspan2_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan2.png')).convert_alpha()
        erklspan3_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan3.png')).convert_alpha()
        erklspan35_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan35.png')).convert_alpha()
        SPL1_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL1.png')).convert_alpha()
        SPL2_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL2.png')).convert_alpha()
        SPL3_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL3.png')).convert_alpha()
        SPL4_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL4.png')).convert_alpha()
        SPL5_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL5.png')).convert_alpha()
        SPL6_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL6.png')).convert_alpha()
        SPL7_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL7.png')).convert_alpha()
        SPL8_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL8.png')).convert_alpha()
        SPL9_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL9.png')).convert_alpha()
        SPL10_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPL10.png')).convert_alpha()
        # span leicht richtig
        zweiv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'2V.png')).convert_alpha()
        vierv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'4V.png')).convert_alpha()
        sexv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'6V.png')).convert_alpha()
        achtv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'8V.png')).convert_alpha()
        zehnv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'10V.png')).convert_alpha()
        zwöv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'12V.png')).convert_alpha()
        vierzv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'14V.png')).convert_alpha()
        sexzv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'16V.png')).convert_alpha()
        achtzv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'18V.png')).convert_alpha()
        zwav_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'20V.png')).convert_alpha()
        # mit
        erklspan4_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan4.png')).convert_alpha()
        erklspan5_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan5.png')).convert_alpha()
        erklspan55_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan55.png')).convert_alpha()
        SPM1_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM1.png')).convert_alpha()
        SPM2_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM2.png')).convert_alpha()
        SPM3_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM3.png')).convert_alpha()
        SPM4_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM4.png')).convert_alpha()
        SPM5_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM5.png')).convert_alpha()
        SPM6_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM6.png')).convert_alpha()
        SPM7_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM7.png')).convert_alpha()
        SPM8_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM8.png')).convert_alpha()
        SPM9_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM9.png')).convert_alpha()
        SPM10_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPM10.png')).convert_alpha()
        # span mit richtig
        vierzigv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'40V.png')).convert_alpha()
        sexzigv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'60V.png')).convert_alpha()
        achtzigv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'80V.png')).convert_alpha()
        hundv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'100V.png')).convert_alpha()
        hundzwav_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'120V.png')).convert_alpha()
        hundvierv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'140V.png')).convert_alpha()
        hunsexv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'160V.png')).convert_alpha()
        hundachtv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'180V.png')).convert_alpha()
        zweihunv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'200V.png')).convert_alpha()
        zweihunzweiv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'220V.png')).convert_alpha()
        # schwer
        erklspan6_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'erklspan6.png')).convert_alpha()
        SPS1_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS1.png')).convert_alpha()
        SPS2_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS2.png')).convert_alpha()
        SPS3_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS3.png')).convert_alpha()
        SPS4_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS4.png')).convert_alpha()
        SPS5_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS5.png')).convert_alpha()
        SPS6_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS6.png')).convert_alpha()
        SPS7_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS7.png')).convert_alpha()
        SPS8_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS8.png')).convert_alpha()
        SPS9_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS9.png')).convert_alpha()
        SPS10_img = pygame.image.load(os.path.join(IMAGE_FOLDER5,'SPS10.png')).convert_alpha()
        # span schwer richtig
        eisv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'1V.png')).convert_alpha()
        dreiv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'3V.png')).convert_alpha()
        fünfv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'5V.png')).convert_alpha()
        neunv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'9V.png')).convert_alpha()
        fünfzv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'15V.png')).convert_alpha()
        vierzwav_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'24V.png')).convert_alpha()
        zweidreiv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'32V.png')).convert_alpha()
        achtvierv_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'48V.png')).convert_alpha()
        # span falsch
        leichtvf_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'l2-20V.png')).convert_alpha()
        mitvf_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'l20-220V.png')).convert_alpha()
        schwervf_img= pygame.image.load(os.path.join(IMAGE_FOLDER2,'l1-48V.png')).convert_alpha()
    except pygame.error as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        sys.exit()
except pygame.error as e:
    print(f"Fehler beim Laden des Bildes: {e}")
    sys.exit()
# sound
try:
    ok_s = pygame.mixer.Sound(os.path.join(IMAGE_FOLDER6, 'ok.wav'))
    menu_s = pygame.mixer.Sound(os.path.join(IMAGE_FOLDER6, 'menu.wav'))
    menu2_s = pygame.mixer.Sound(os.path.join(IMAGE_FOLDER6, 'menu2.wav'))
except (pygame.error, FileNotFoundError) as e:
    print(f"Sound-Warnung: {e} - Programm läuft ohne Sound weiter")
    ok_s = None
    menu_s = None
    menu2_s = None
except pygame.error as e:
    print(f"Fehler beim Laden des Bildes: {e}")
    sys.exit()
# buttons
try:
# main menu    
    try:
        # start
        start_button = button.Button(700,500,start_img,1)
        # interface
        exit_button = button.Button(118,855,exit_img,0.8)
        zurü_button = button.Button(1470,100,zurü_img,1)
        weit_button  = button.Button(1629,100,weit_img,1)
        hmenu_button = button.Button(118,855,hmenu_img,0.8)
        menuw_button  = button.Button(700, 450,menuw_img,1)
        menustr_button  = button.Button(700, 450,menustr_img,1)
        menusp_button  = button.Button(700, 450,menusp_img,1)       
        urihelp_button  = button.Button(120,70,urihelp_img,0.2)
        urierkl_button  = button.Button(1320,290,erklärung_img,0.6)
        urifort_button  = button.Button(1420,490,urifort_img,0.6)
        urirech_button  = button.Button(1320,690,urirech_img,0.6) 
        tech_button  = button.Button(865,825,tech_img,0.2)
        # links ges form gefa
        muse_button  = button.Button(300, 750,muse_img,1)  
        wiki_button  = button.Button(1300, 550,wiki_img,1)  
        meg_button  = button.Button(200, 250,meg_img,1)  
        stud_button  = button.Button(300, 650,stud_img,1)  
        leifi_button  = button.Button(1300, 750,leifi_img,1)   
        serlo_button  = button.Button(400, 150,serlo_img,1) 
        leifi1_button  = button.Button(1300, 750,leifi_img,1)         
        srf_button  = button.Button(200, 550,srf_img,0.4) 
        suva_button  = button.Button(300, 150,suva_img,0.4) 
        # link spielen
        phet_button  = button.Button(350, 750,phet_img,1)
        mal_button  = button.Button(350, 150,mal_img,1) 
        box_button  = button.Button(150, 400,box_img,1) 
        # menu lern
        lern_button = button.Button(775, 550,lern_img,0.75)
        spi_button  = button.Button(642, 350,spi_img,1.2)
        # menu geschformgefa
        ges_button = button.Button(700, 250,ges_img,1)
        form_button = button.Button(700, 450,form_img,1)
        gefabutton = button.Button(700, 650,gefa_img,1)
        # menu spawid
        span_button = button.Button(700, 650,span_img,1)
        wider_button = button.Button(700, 250,wider_img,1)
        strom_button = button.Button(700, 450,strom_img,1)
        # menu widerstand
        erklwider_button = button.Button(700, 150,erklärung_img,1)
        leiwider_button = button.Button(700, 350,lei_img,1)
        mitwider_button = button.Button(700, 550,mit_img,1)
        schwewider_button = button.Button(700, 750,schwe_img,1)
        # menu stromstärke
        erklstrom_button = button.Button(700, 150,erklärung_img,1)
        leistrom_button = button.Button(700, 350,lei_img,1)
        mitstrom_button = button.Button(700, 550,mit_img,1)
        schwestrom_button = button.Button(700, 750,schwe_img,1)
        # menu spannung
        erklspan_button = button.Button(700, 150,erklärung_img,1)
        leispan_button = button.Button(700, 350,lei_img,1)
        mitspan_button = button.Button(700, 550,mit_img,1)
        schwespan_button = button.Button(700, 750,schwe_img,1)
    except pygame.error as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        sys.exit()
# widerstand
    try:
        # wider leicht richtig
        zwei_button = button.Button(1500, 585,zwei_img,1.08,)
        vier_button = button.Button(1500, 663,vier_img,1.08)
        sex_button = button.Button(1500, 400,sex_img,1.08)
        acht_button = button.Button(1501, 824,acht_img,1)
        zeh_button = button.Button(1500, 901,zeh_img,1.08)
        zwö_button = button.Button(1642, 584,zwö_img,1.08)
        vierz_button = button.Button(1642, 686,vierz_img,1.08)
        sexz_button = button.Button(1642, 400,sexz_img,1.08)
        achtz_button = button.Button(1640,822,achtz_img,1.06)
        zwan_button = button.Button(1642, 400,zwan_img,1.08)
        # wider mit richtig
        hun_button = button.Button(1500, 507,hun_img,1.08)
        hunz_button = button.Button(1500, 584,hunz_img,1.08)
        hunzwa_button = button.Button(1500, 664,hunzwa_img,1.06)
        hundre_button = button.Button(1500, 400,hundre_img,1.08)
        hunvie_button = button.Button(1500, 823,hunvie_img,1.06)
        hunfün_button = button.Button(1500, 901,hunfün_img,1.08)
        hunsex_button = button.Button(1640, 584,hunsex_img,1.08)
        hunsib_button = button.Button(1642, 400,hunsib_img,1.08)
        hunacht_button = button.Button(1642, 400,hunacht_img,1.08)
        hunneu_button = button.Button(1642, 400,hunneu_img,1.08)
        zweihun_button = button.Button(1642, 400,zweihun_img,1.08)  
        # wider schwer richtig 
        zweihunein_button = button.Button(1499, 591,zweihunein_img,1.08)
        hunzwadrei_button = button.Button(1500, 515,hunzwadrei_img,1.06)
        hundreivie_button = button.Button(1500, 748,hundreivie_img,1.08)        
        sibsib_button = button.Button(1500, 828,sibsib_img,1.08)
        neusib_button = button.Button(1500, 908,neusib_img,1.08)
        hunfüneu_button = button.Button(1640, 513,hunfüneu_img,1.08)
        hunsibsib_button = button.Button(1640, 669,hunsibsib_img,1.08)
        hunzwavie_button = button.Button(1640, 747,hunzwavie_img,1.08)
        hunvievie_button = button.Button(1640, 828,hunvievie_img,1.08)
        hunzwafü_button = button.Button(1640, 908,hunzwafü_img,1.06)
        # wider falsch
        l220_button = button.Button(1495,500,l220_img,1.1,hover_enabled=False)
        l100200_button = button.Button(1495, 500,l100200_img,1.1,hover_enabled=False)
        lschwer_button = button.Button(1495, 505,lschwer_img,1.1,hover_enabled=False)
    except pygame.error as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        sys.exit()
# strom
    try:
        # strom leicht mit schwer richtig
        LA_button = button.Button(1518, 465,LA_img,0.85)
        LB_button = button.Button(1518, 537,LB_img,0.85)
        LC_button = button.Button(1518, 607,LC_img,0.85)
        LD_button = button.Button(1518, 679,LD_img,0.85)
        LE_button = button.Button(1518, 750,LE_img,0.85)
        LF_button = button.Button(1518, 823,LF_img,0.85)
        LG_button = button.Button(1652, 465,LG_img,0.85)
        LH_button = button.Button(1652, 537,LH_img,0.85)
        LI_button = button.Button(1652, 609,LI_img,0.85)
        LJ_button = button.Button(1652, 753,LJ_img,0.85)
        LK_button = button.Button(1652, 823,LK_img,0.85)
        Lalle_button = button.Button(1652, 823,alle_img,0.85) 
        # strom falsch
        stromfalsch_button = button.Button(1500, 485,stromfalsch_img,1.06,hover_enabled=False)
    except pygame.error as e:
      print(f"Fehler beim Laden des Bildes: {e}")
      sys.exit()
# spannung
    try:
        # span leicht richtig
        zweiv_button = button.Button(1500, 587,zweiv_img,1.07)
        vierv_button = button.Button(1500, 666,vierv_img,1.08)
        sexv_button = button.Button(1500, 746,sexv_img,1.07)
        achtv_button = button.Button(1501, 824,achtv_img,1)
        zehnv_button = button.Button(1500, 903,zehnv_img,1.08)
        zwöv_button = button.Button(1636, 586,zwöv_img,1.08)
        vierzv_button = button.Button(1636, 664,vierzv_img,1.08)
        sexzv_button = button.Button(1636, 746,sexzv_img,1.08)
        achtzv_button = button.Button(1640,822,achtzv_img,1.06)
        zwav_button = button.Button(1642, 903,zwav_img,1.08)
        # span mit richtig
        zwav_button = button.Button(1500, 507,zwav_img,1.08)
        vierzigv_button = button.Button(1500, 584,vierzigv_img,1.08)
        sexzigv_button = button.Button(1500, 664,sexzigv_img,1.06)
        achtzv_button = button.Button(1500, 400,achtzv_img,1.08)
        hundv_button = button.Button(1501, 824,hundv_img,1.06)
        hunzwav_button = button.Button(1500, 903,hundzwav_img,1.08)
        hunvierv_button = button.Button(1635, 585,hundvierv_img,1.07)
        hunsexv_button = button.Button(1636, 664,hunsexv_img,1.08)
        hunachtv_button = button.Button(1636, 741,hundachtv_img,1.08)
        zweihunv_button = button.Button(1636, 824,zweihunv_img,1.07)
        zweihunzweiv_button = button.Button(1642, 400,zweihunzweiv_img,1.08)
        # span schwer richtig
        eisv_button = button.Button(1500, 507,eisv_img,1.06)
        dreiv_button = button.Button(1499, 584,dreiv_img,1.08)
        fünfv_button = button.Button(1500, 668,fünfv_img,1.07)
        sexv2_button = button.Button(1500, 748,sexv_img,1.07)
        neunv_button = button.Button(1500, 907,neunv_img,1.08)
        zwöv2_button = button.Button(1636, 513,zwöv_img,1.07)
        fünfzv_button = button.Button(1636, 590,fünfzv_img,1.07)
        achtzv2_button = button.Button(1636, 670,achtzv_img,1.08)
        vierzwav_button = button.Button(1636, 750,vierzwav_img,1.08)
        zweidreiv_button = button.Button(1640, 823,zweidreiv_img,1.08)
        achtvierv_button = button.Button(1640, 901,achtvierv_img,1.06)       
        # span falsch
        leichtv_button = button.Button(1495,500,leichtvf_img,1.1,hover_enabled=False)
        mitv_button = button.Button(1495, 500,mitvf_img,1.1,hover_enabled=False)
        schwerv_button = button.Button(1495, 505,schwervf_img,1.1,hover_enabled=False)
    except pygame.error as e:
       print(f"Fehler beim Laden des Bildes: {e}")
       sys.exit()
except pygame.error as e:
    print(f"Fehler beim Laden des Bildes: {e}")
    sys.exit()
# laden oder erstelle scoredatei 
Scores = scores.Scores()
# start parameters
clicked = False
running = True
menu_state ="start"
# gameloop
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg_img,(0,0))
    if urihelp_button.draw(screen) and menu_s.play() and clicked == False:
        menu_state = "urihelp" 
        clicked = True
# main menu
    if True:  
    # menu navigation
        # main zu lern 
        if menu_state == "start":
                screen.blit(neubg_img,(0,0))        
                if start_button.draw(screen) and clicked == False:   
                    menu_state = "main" 
                    clicked = True
    # main zu lern spi
        if menu_state == "main":
                screen.blit(uristart_img,(1300,200))
                if lern_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "lern"
                    clicked = True
                if spi_button.draw(screen)and menu_s.play() and clicked == False:
                    menu_state = "spielen"
                    clicked = True
    # urihelpmenu
        if menu_state == "urihelp": 
                screen.blit(playbg_img,(200,200))
                if phet_button.draw(screen):
                    webbrowser.open_new_tab("https://phet.colorado.edu/sims/html/circuit-construction-kit-dc-virtual-lab/latest/circuit-construction-kit-dc-virtual-lab_de.html")
                if mal_button.draw(screen):
                    webbrowser.open_new_tab("https://falstad.com/circuit/")
                if box_button.draw(screen):
                    webbrowser.open_new_tab("https://www.lerneninderbox.ch/lernapps/elektrizit%C3%A4t/")
                if tech_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "tech_support"
                    clicked = True
                if urifort_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "fortschritte"
                    clicked = True
                if urirech_button.draw(screen):
                    webbrowser.open_new_tab("https://www.digikey.de/de/resources/conversion-calculators/conversion-calculator-parallel-and-series-resistor")
                if urierkl_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "urierkl"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "tech_support":
                # Titel
                font_title = pygame.font.Font(None, 70)
                title_text = font_title.render("Technischer Support", True, (255, 215, 0))
                title_rect = title_text.get_rect(center=(960, 280))
                screen.blit(title_text, title_rect)
                # Nachricht
                font_text = pygame.font.Font(None, 45)
                messages = [
                    "Bei technischen Problemen oder Fragen",
                    "kontaktiere uns bitte per E-Mail:",
                    "",
                    "Marco.Ladner@stud.isme-edu.ch",
                    "",
                    "Wir helfen dir gerne weiter!"] 
                y_pos = 400
                for msg in messages:
                    if "@" in msg:  # E-Mail hervorheben
                        text = font_text.render(msg, True, (100, 200, 255))  # Hellblau
                    elif msg == "":  # Leerzeile
                        y_pos += 20
                        continue
                    else:
                        text = font_text.render(msg, True, (255, 255, 255))
                    text_rect = text.get_rect(center=(960, y_pos))
                    screen.blit(text, text_rect)
                    y_pos += 60
                # Buttons
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "urihelp"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "urierkl":
                screen.blit(erkl1_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "urihelp"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                     menu_state = "erklw2"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "fortschritte":
                # Titel
                font_title = pygame.font.Font(None, 80)
                title_text = font_title.render("Meine Fortschritte", True, (255, 215, 0))  # Gold
                screen.blit(title_text, (650, 250))
                # Fonts
                font_large = pygame.font.Font(None, 50)
                font_medium = pygame.font.Font(None, 40)
                font_small = pygame.font.Font(None, 32)
                y_pos = 350
                x_left = 450
                spacing = 100
                # Funktion für Fortschrittsbalken
                def draw_progress_bar(x, y, width, height, percentage, color_empty, color_fill):
                    # Äußerer Rahmen
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 3)
                    # Gefüllter Teil
                    fill_width = int(width * (percentage / 100))
                    if fill_width > 0:
                        pygame.draw.rect(screen, color_fill, (x+3, y+3, fill_width-6, height-6))
                # Sannung
                span_total = Scores.spanscore + Scores.spanwrong
                if span_total > 0:
                    span_percentage = (Scores.spanscore / span_total) * 100
                else:
                    span_percentage = 0
                span_label = font_large.render("Spannung", True, (255, 255, 255))
                screen.blit(span_label, (x_left, y_pos))
                span_stats = font_medium.render(f"{Scores.spanscore} richtig | {Scores.spanwrong} falsch | {span_percentage:.0f}%", 
                                               True, (200, 200, 200))
                screen.blit(span_stats, (x_left, y_pos + 45))
                # Fortschrittsbalken
                bar_color = (0, 255, 0) if span_percentage >= 70 else (255, 165, 0) if span_percentage >= 50 else (255, 50, 50)
                draw_progress_bar(x_left, y_pos + 85, 600, 30, span_percentage, (50, 50, 50), bar_color)
                y_pos += spacing + 40
                # Widerstand
                wider_total = Scores.widerscore + Scores.widerwrong
                if wider_total > 0:
                    wider_percentage = (Scores.widerscore / wider_total) * 100
                else:
                    wider_percentage = 0
                wider_label = font_large.render("Widerstand", True, (255, 255, 255))
                screen.blit(wider_label, (x_left, y_pos))
                wider_stats = font_medium.render(f"{Scores.widerscore} richtig | {Scores.widerwrong} falsch | {wider_percentage:.0f}%", 
                                                True, (200, 200, 200))
                screen.blit(wider_stats, (x_left, y_pos + 45))
                bar_color = (0, 255, 0) if wider_percentage >= 70 else (255, 165, 0) if wider_percentage >= 50 else (255, 50, 50)
                draw_progress_bar(x_left, y_pos + 85, 600, 30, wider_percentage, (50, 50, 50), bar_color)
                y_pos += spacing + 40
                # Stromstärke
                strom_total = Scores.stromscore + Scores.stromwrong
                if strom_total > 0:
                    strom_percentage = (Scores.stromscore / strom_total) * 100
                else:
                    strom_percentage = 0
                strom_label = font_large.render("Stromstaerke", True, (255, 255, 255))
                screen.blit(strom_label, (x_left, y_pos))
                strom_stats = font_medium.render(f"{Scores.stromscore} richtig | {Scores.stromwrong} falsch | {strom_percentage:.0f}%", 
                                                True, (200, 200, 200))
                screen.blit(strom_stats, (x_left, y_pos + 45))
                bar_color = (0, 255, 0) if strom_percentage >= 70 else (255, 165, 0) if strom_percentage >= 50 else (255, 50, 50)
                draw_progress_bar(x_left, y_pos + 85, 600, 30, strom_percentage, (50, 50, 50), bar_color)
                y_pos += spacing + 60
                # Gesamtstatistik
                total_correct = Scores.spanscore + Scores.widerscore + Scores.stromscore
                total_wrong = Scores.spanwrong + Scores.widerwrong + Scores.stromwrong
                total_all = total_correct + total_wrong
                if total_all > 0:
                    total_percentage = (total_correct / total_all) * 100 
                    # Trennlinie
                    pygame.draw.line(screen, (255, 255, 255), (x_left - 50, y_pos - 20), (x_left + 650, y_pos - 20), 2) 
                    gesamt_label = font_large.render("Gesamt", True, (255, 215, 0))
                    screen.blit(gesamt_label, (x_left, y_pos)) 
                    gesamt_stats = font_medium.render(f"{total_correct}/{total_all} richtig ({total_percentage:.1f}%)", 
                                                     True, (200, 200, 200))
                    screen.blit(gesamt_stats, (x_left, y_pos + 45))    
                    # Motivierende Nachricht basierend auf Leistung
                    if total_percentage >= 90:
                        motivation = "Ausgezeichnet! Du bist ein Experte!"
                        mot_color = (0, 255, 0)
                    elif total_percentage >= 75:
                        motivation = "Sehr gut! Weiter so!"
                        mot_color = (100, 255, 100)
                    elif total_percentage >= 60:
                        motivation = "Gute Arbeit! Noch etwas ueben."
                        mot_color = (255, 200, 0)
                    elif total_percentage >= 50:
                        motivation = "Mach weiter! Du machst Fortschritte."
                        mot_color = (255, 165, 0)
                    else:
                        motivation = "Nicht aufgeben! Uebung macht den Meister."
                        mot_color = (255, 100, 100)    
                    mot_text = font_medium.render(motivation, True, mot_color)
                    mot_rect = mot_text.get_rect(center=(960, y_pos + 100))
                    screen.blit(mot_text, mot_rect)
                else:
                    # Keine Aufgaben gelöst
                    no_data = font_large.render("Noch keine Aufgaben geloest", True, (200, 200, 200))
                    no_data_rect = no_data.get_rect(center=(960, y_pos))
                    screen.blit(no_data, no_data_rect)  
                    start_hint = font_medium.render("Starte mit den Uebungen, um deinen Fortschritt zu sehen!", 
                                                   True, (150, 150, 150))
                    hint_rect = start_hint.get_rect(center=(960, y_pos + 60))
                    screen.blit(start_hint, hint_rect)
                # Buttons
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "urihelp"
                    clicked = True  
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
    # lern zu geschichte formeln gefahren
        if menu_state == "lern":
                screen.blit(uriwiss_img,(300,200))
                if ges_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "geschichte"
                    clicked = True
                if form_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "formeln"
                    clicked = True
                if gefabutton.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "gefahren"
                    clicked = True
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
    # zu lernseite
        if menu_state == "geschichte":
                screen.blit(gesbg_img,(200,200))
                if meg_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://www.energiegeschichte.de/de/meg-energiegeschichte/energiethemen.html")
                if muse_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://blog.nationalmuseum.ch/2021/10/elektrifizierung-2-0/")
                if wiki_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://de.wikipedia.org/wiki/Elektrotechnik")
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "lern" 
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "formeln":
                screen.blit(formbg_img,(200,200))
                if leifi_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://www.leifiphysik.de/elektrizitaetslehre")
                if serlo_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://de.serlo.org/physik/48617/elektrizitaetslehre")
                if stud_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://studyflix.de/physik/thema/elektrotechnik-158")
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "lern" 
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "gefahren":
                screen.blit(gefabg_img,(200,200))
                if leifi1_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://www.leifiphysik.de/elektrizitaetslehre/ohmsches-gesetz-kennlinien/grundwissen/gefahr-durch-strom-und-koerperwiderstand")
                if srf_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://www.srf.ch/play/tv/srf-school/video/strom-achtung-gefahr-88?urn=urn:srf:video:1c30c9fb-0b32-41ba-abbc-bd6c45f8ce15")
                if suva_button.draw(screen) and menu_s.play():
                    webbrowser.open_new_tab("https://www.suva.ch/de-ch/praevention/nach-gefahren/gefaehrliche-materialien-strahlungen-und-situationen/umgang-mit-elektrizitaet")
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "lern" 
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
    # menu spannun widerstand stromstärke gemischt    
        if menu_state == "spielen":
                screen.blit(urigebiet_img,(1300,200))
                if span_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "spannung"
                    clicked = True
                if wider_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "widerstand"
                    clicked = True
                if strom_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "stromstärke"
                    clicked = True
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "main" 
                if exit_button.draw(screen)and clicked == False:
                    running = False
    #menu spannung zu level  
        if menu_state == "widerstand":
                screen.blit(urigrad_img,(200,150))
                if erklwider_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "erklwider"
                    clicked = True
                if leiwider_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "widerleicht"
                    clicked = True
                if mitwider_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "widermit"
                    clicked = True
                if schwewider_button.draw(screen) and menu_s.play() and clicked == False:
                    menu_state = "widerschwer"
                    clicked = True
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "spielen"
                    clicked = True
                if exit_button.draw(screen)and clicked == False:
                    running = False
        if menu_state == "stromstärke":
                screen.blit(urigrad_img,(200,150))
                if erklstrom_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "erklstrom"
                    clicked = True
                if leistrom_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "stromleicht"
                    clicked = True
                if mitstrom_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "erklstrom1def"
                    clicked = True
                if schwestrom_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "erklstr1skip"
                    clicked = True
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "spielen"
                    clicked = True
                if exit_button.draw(screen)and clicked == False:
                    running = False
        if menu_state == "spannung":
                screen.blit(urigrad_img,(200,150))
                if erklspan_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "erklspan"
                    clicked = True
                if leispan_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "erklspan35"
                    clicked = True
                if mitspan_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "erklspan4"
                    clicked = True
                if schwespan_button.draw(screen) and menu_s.play()  and clicked == False:
                    menu_state = "erklspan6"
                    clicked = True
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "spielen"
                    clicked = True
                if exit_button.draw(screen)and clicked == False:
                    running = False
# widerstand
    # erklwider
    if True:          
        if menu_state == "erklwider":
                screen.blit(erkl1_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "widerstand"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                     menu_state = "erklw2"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "erklw2":
                screen.blit(erkl2_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklwider"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklw3"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "erklw3":
                screen.blit(erkl3_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklw2"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklwiderser"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "erklwiderser":
                screen.blit(erklwser_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklw3"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklwiderpara"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "erklwiderpara":
                screen.blit(erklwpara_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklwiderser"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "widerstand"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
    # widerleicht
    if True:
        if menu_state == "widerleicht":
                screen.blit(erklwgruppe_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "widerstand"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE1"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True     
        if menu_state == "WE1":
                screen.blit(WE1_img,(10,10))
                if  zwö_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play() and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "widerleicht"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
        if menu_state == "WE2":            
                screen.blit(WE2_img,(10,10))
                if  zwei_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WE3":            
                screen.blit(WE3_img,(10,10))
                if  acht_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "WE4":
                screen.blit(WE4_img,(10,10))
                if  zwei_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WE5":
                screen.blit(WE5_img,(10,10))
                if  vier_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WE6":        
                screen.blit(WE6_img,(10,10))
                if  zwö_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WE7":            
                screen.blit(WE7_img,(10,10))
                if  vier_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WE8":            
                screen.blit(WE8_img,(10,10))
                if  zwö_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WE9":        
                screen.blit(WE9_img,(10,10))
                if  achtz_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WE10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WE10":            
                screen.blit(WE10_img,(10,10))
                if  zeh_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l220_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatwiderl"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WE9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatwiderl":
                screen.blit(urina_img,(1250,200)) 
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "WE10"                
                    clicked = True
                if menuw_button.draw(screen) and menu_s.play() :                   
                    menu_state = "widerstand"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
    # widermit
    if True:
        if menu_state == "widermit":
                screen.blit(erklwskip_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "widerstand"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM1"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WM1":
                screen.blit(WM1_img,(10,10))
                if  hun_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "widermit"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WM2":            
                screen.blit(WM2_img,(10,10))
                if  hunfün_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WM3":            
                screen.blit(WM3_img,(10,10))
                if  hun_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "WM4":
                screen.blit(WM4_img,(10,10))
                if  hun_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WM5":
                screen.blit(WM5_img,(10,10))
                if  hunfün_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WM6":        
                screen.blit(WM6_img,(10,10))
                if  hunvie_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WM7":            
                screen.blit(WM7_img,(10,10))
                if  hunsex_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WM8":            
                screen.blit(WM8_img,(10,10))
                if  hunz_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WM9":        
                screen.blit(WM9_img,(10,10))
                if  hun_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WM10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WM10":            
                screen.blit(WM10_img,(10,10))
                if  hunsex_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif l100200_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatwiderm"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WM9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatwiderm": 
                screen.blit(uriweit_img,(1300,200))
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "WM10"                
                    clicked = True
                if menuw_button.draw(screen) and menu_s.play() :                   
                    menu_state = "widerstand"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
    # widerschwer
    if True:
        if menu_state == "widerschwer":
                screen.blit(erklwschwer_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "widerstand"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS1"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WS1":
                screen.blit(WS1_img,(10,10))
                if  hunsibsib_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "widerschwer"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WS2":            
                screen.blit(WS2_img,(10,10))
                if  hunzwavie_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WS3":            
                screen.blit(WS3_img,(10,10))
                if  hunzwafü_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "WS4":
                screen.blit(WS4_img,(10,10))
                if  sibsib_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WS5":
                screen.blit(WS5_img,(10,10))
                if  hundreivie_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WS6":        
                screen.blit(WS6_img,(10,10))
                if  hunvievie_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WS7":            
                screen.blit(WS7_img,(10,10))
                if  neusib_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WS8":            
                screen.blit(WS8_img,(10,10))
                if  zweihunein_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "WS9":        
                screen.blit(WS9_img,(10,10))
                if  hunzwadrei_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "WS10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "WS10":            
                screen.blit(WS10_img,(10,10))
                if  hunfüneu_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_wider()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif lschwer_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_widerwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatwiders"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "WS9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatwiders": 
                screen.blit(uripr_img,(1300,200))
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "WS10"                
                    clicked = True
                if menuw_button.draw(screen) and menu_s.play() :                   
                    menu_state = "widerstand"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
# stromstärke
    # erklstr
    if True: 
    # stromerkl                
        if menu_state == "erklstrom":
                screen.blit(erkl1_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "stromstärke"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklst2"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "erklst2":
                screen.blit(erkl2_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklstrom"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklst3"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "erklst3":
                screen.blit(erkl3_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklst2"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklstromser"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "erklstromser":
                screen.blit(erklstrser_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklst3"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklstrompara"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "erklstrompara":
                screen.blit(erklstrpara_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklstromser"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklstrgruppe"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "erklstrgruppe":
                screen.blit(erklstrgruppe_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklstrompara"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "stromstärke"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True     
    # strleicht
    if True:    
        if menu_state == "stromleicht":
                screen.blit(erklstrleicht_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "stromstärke"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL1"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STL1":
                screen.blit(STL1_img,(10,10))
                if  Lalle_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "stromleicht"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
        if menu_state == "STL2":            
                screen.blit(STL2_img,(10,10))
                if  LB_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "STL3":            
                screen.blit(STL3_img,(10,10))
                if  LB_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "STL4":
                screen.blit(STL4_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STL5":
                screen.blit(STL5_img,(10,10))
                if  Lalle_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STL6":        
                screen.blit(STL6_img,(10,10))
                if  LE_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STL7":            
                screen.blit(STL7_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STL8":            
                screen.blit(STL8_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "STL9":        
                screen.blit(STL9_img,(10,10))
                if  LD_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STL10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STL10":            
                screen.blit(STL10_img,(10,10))
                if  LB_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatstrl"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STL9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatstrl": 
                screen.blit(uriber_img,(1300,200))
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "STL10"                
                    clicked = True
                if menustr_button.draw(screen) and menu_s.play() :                   
                    menu_state = "stromstärke"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
    # strmit
    if True:
        if menu_state == "erklstrom1def":
                screen.blit(erklstr1def_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "stromstärke"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklstrom2def"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True          
        if menu_state == "erklstrom2def":
                screen.blit(erklstr2def_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklstrom1def"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM1"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "STM1":
                screen.blit(STM1_img,(10,10))
                if  LC_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklstrom2def"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
        if menu_state == "STM2":            
                screen.blit(STM2_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "STM3":            
                screen.blit(STM3_img,(10,10))
                if  LC_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "STM4":
                screen.blit(STM4_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STM5":
                screen.blit(STM5_img,(10,10))
                if  Lalle_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STM6":        
                screen.blit(STM6_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STM7":            
                screen.blit(STM7_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STM8":            
                screen.blit(STM8_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "STM9":        
                screen.blit(STM9_img,(10,10))
                if  LD_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STM10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STM10":            
                screen.blit(STM10_img,(10,10))
                if  LD_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatstrm"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STM9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatstrm":
                screen.blit(urigr_img,(1300,200)) 
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "STM10"                
                    clicked = True
                if menustr_button.draw(screen) and menu_s.play() :                   
                    menu_state = "stromstärke"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
    # strschwer 
    if True:
        if menu_state == "erklstr1skip":
                screen.blit(erklstr1skip_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "stromstärke"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS1"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True          
        if menu_state == "STS1":
                screen.blit(STS1_img,(10,10))
                if  LE_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklstr1skip"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
        if menu_state == "STS2":            
                screen.blit(STS2_img,(10,10))
                if  LB_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "STS3":            
                screen.blit(STS3_img,(10,10))
                if  LB_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "STS4":
                screen.blit(STS4_img,(10,10))
                if  LC_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STS5":
                screen.blit(STS5_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STS6":        
                screen.blit(STS6_img,(10,10))
                if  Lalle_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STS7":            
                screen.blit(STS7_img,(10,10))
                if  LC_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STS8":            
                screen.blit(STS8_img,(10,10))
                if  LG_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "STS9":        
                screen.blit(STS9_img,(10,10))
                if  LA_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "STS10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "STS10":            
                screen.blit(STS10_img,(10,10))
                if  Lalle_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_strom()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif stromfalsch_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_stromwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatstrs"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "STS9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatstrs": 
                screen.blit(urisuper_img,(1300,200))
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "STS10"                
                    clicked = True
                if menustr_button.draw(screen) and menu_s.play() :                   
                    menu_state = "stromstärke"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
# spannung
    #erklspan
    if True:
        if menu_state == "erklspan":
                screen.blit(erkl1_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "spannung"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklsp2"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True   
        if menu_state == "erklsp2":
                screen.blit(erkl2_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklsp3"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
        if menu_state == "erklsp3":
                screen.blit(erkl3_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklsp2"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklspan1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True   
        if menu_state == "erklspan1":
                screen.blit(erklspan1_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklsp3"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklspan2"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True   
        if menu_state == "erklspan2":
                screen.blit(erklspan2_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan1"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklspan3"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "erklspan3":
                screen.blit(erklspan3_img,(10,10))
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan2"
                    clicked = True
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "spannung"
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
    # spanleicht
    if True:
        if menu_state == "erklspan35":
                screen.blit(erklspan35_img,(10,10))
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL1"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "spannung"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPL1":
                screen.blit(SPL1_img,(10,10))
                if  sexv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan35"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
        if menu_state == "SPL2":            
                screen.blit(SPL2_img,(10,10))
                if  zehnv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPL3":            
                screen.blit(SPL3_img,(10,10))
                if  vierv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "SPL4":
                screen.blit(SPL4_img,(10,10))
                if  sexv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPL5":
                screen.blit(SPL5_img,(10,10))
                if  sexv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPL6":        
                screen.blit(SPL6_img,(10,10))
                if  zweiv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPL7":            
                screen.blit(SPL7_img,(10,10))
                if  vierzv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPL8":            
                screen.blit(SPL8_img,(10,10))
                if  sexzv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPL9":        
                screen.blit(SPL9_img,(10,10))
                if  zwöv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPL10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPL10":            
                screen.blit(SPL10_img,(10,10))
                if  zwöv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif leichtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatspanl"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPL9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatspanl": 
                screen.blit(urimw_img,(1300,200))
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "SPL10"                
                    clicked = True
                if menuw_button.draw(screen) and menu_s.play() :                   
                    menu_state = "spannung"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
    # spanmit
    if True:
        if menu_state == "erklspan4":
                screen.blit(erklspan4_img,(10,10))
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklspan5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "spannung"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "erklspan5":
                screen.blit(erklspan5_img,(10,10))
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "erklspan55"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "erklspan55":
                screen.blit(erklspan55_img,(10,10))
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM1"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan5"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPM1":
                screen.blit(SPM1_img,(10,10))
                if  sexzigv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan55"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
        if menu_state == "SPM2":            
                screen.blit(SPM2_img,(10,10))
                if  hunachtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPM3":            
                screen.blit(SPM3_img,(10,10))
                if  hunsexv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "SPM4":
                screen.blit(SPM4_img,(10,10))
                if  hundv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPM5":
                screen.blit(SPM5_img,(10,10))
                if  hunvierv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPM6":        
                screen.blit(SPM6_img,(10,10))
                if  zweihunv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPM7":            
                screen.blit(SPM7_img,(10,10))
                if  hunzwav_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPM8":            
                screen.blit(SPM8_img,(10,10))
                if  hunzwav_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPM9":        
                screen.blit(SPM9_img,(10,10))
                if  hunachtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPM10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPM10":            
                screen.blit(SPM10_img,(10,10))
                if  hunachtv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif mitv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatspanm"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPM9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatspanm": 
                screen.blit(urigut_img,(1300,200))
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "SPM10"                
                    clicked = True
                if menuw_button.draw(screen) and menu_s.play() :                   
                    menu_state = "spannung"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
    # spanschwer
    if True:
        if menu_state == "erklspan6":
                screen.blit(erklspan6_img,(10,10))
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS1"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "spannung"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPS1":
                screen.blit(SPS1_img,(10,10))
                if  fünfv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS2"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "erklspan6"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True         
        if menu_state == "SPS2":            
                screen.blit(SPS2_img,(10,10))
                if  fünfv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS3"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS1"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPS3":            
                screen.blit(SPS3_img,(10,10))
                if  fünfzv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS4"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS2"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True      
        if menu_state == "SPS4":
                screen.blit(SPS4_img,(10,10))
                if  achtzv2_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS5"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS3"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPS5":
                screen.blit(SPS5_img,(10,10))
                if  vierzwav_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS6"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS4"
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPS6":        
                screen.blit(SPS6_img,(10,10))
                if  neunv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS7"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS5"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPS7":            
                screen.blit(SPS7_img,(10,10))
                if  neunv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS8"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS6"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPS8":            
                screen.blit(SPS8_img,(10,10))
                if  zwöv2_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS9"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS7"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True
        if menu_state == "SPS9":        
                screen.blit(SPS9_img,(10,10))
                if  sexv2_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "SPS10"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS8"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True  
        if menu_state == "SPS10":            
                screen.blit(SPS10_img,(10,10))
                if  vierzwav_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(richtig_img,(700,450)) and ok_s.play()
                    Scores.add_span()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                elif schwerv_button.draw(screen) and menu_s.play()  and clicked == False:
                    screen.blit(falsch_img,(700,449))
                    Scores.add_spanwrong()
                    pygame.display.update()
                    pygame.time.wait(2000) 
                if weit_button.draw(screen) and menu_s.play() :
                    menu_state = "resultatspans"
                if zurü_button.draw(screen) and menu2_s.play():
                    menu_state = "SPS9"
                    clicked = True                
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True    
        if menu_state == "resultatspans": 
                screen.blit(urisp_img,(1300,200))
                if zurü_button.draw(screen) and menu2_s.play():                   
                    menu_state = "SPS10"                
                    clicked = True
                if menuw_button.draw(screen) and menu_s.play() :                   
                    menu_state = "spannung"                
                    clicked = True
                if hmenu_button.draw(screen) and menu2_s.play():
                    menu_state = "main"
                    clicked = True 
# update all images
    pygame.display.update()
# eventloop
# mousup check
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
             clicked = False
# close window x
        if event.type == pygame.QUIT:
            running = False
# close window esc           
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_ESCAPE:  # ESC zum Beenden
                running = False
pygame.quit()
sys.exit()   